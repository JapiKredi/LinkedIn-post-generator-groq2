import streamlit as st
from src.data_loader import BlogDataLoader
from src.post_generator import PostGenerator


class StreamlitUI:
    def __init__(self):
        try:
            self.blog_loader = BlogDataLoader()
            self.post_generator = PostGenerator()
            st.success("UI initialized successfully!")
        except Exception as e:
            st.error(f"Error initializing UI: {str(e)}")

    def display_blog_content(self, content):
        """Display blog content in a structured format."""
        if isinstance(content, dict):
            for section, content_data in content.items():
                st.write(f"**{section}:**")
                if isinstance(content_data, list):
                    for item in content_data:
                        st.write(f"- {item}")
                elif isinstance(content_data, dict):
                    for key, value in content_data.items():
                        st.write(f"- {key}: {value}")
                else:
                    st.write(content_data)

    def show_existing_posts(self):
        """Display existing blog posts."""
        try:
            st.header("Existing LinkedIn Posts")
            blogs = self.blog_loader.load_blog_posts()

            if not blogs:
                st.warning(
                    "No existing blog posts found. Please check your data/blog_posts.json file."
                )
                return

            st.info(f"Found {len(blogs)} posts")

            for blog in blogs:
                with st.expander(blog["title"]):
                    if isinstance(blog.get("content"), dict):
                        for section, content in blog["content"].items():
                            st.subheader(section.replace("_", " ").title())
                            if isinstance(content, list):
                                for item in content:
                                    st.write(f"• {item}")
                            else:
                                st.write(content)

                    if "hashtags" in blog:
                        st.write("\n**Hashtags:**")
                        st.write(" ".join(blog["hashtags"]))

        except Exception as e:
            st.error(f"Error showing existing posts: {str(e)}")
            st.error(
                "Please ensure your blog_posts.json file exists and is properly formatted."
            )

    def show_post_generator(self):
        """Show post generation interface."""
        try:
            st.header("Generate New LinkedIn Post")

            if st.button("Generate Post"):
                with st.spinner("Generating new post..."):
                    new_post = self.post_generator.generate_post()
                    st.success("New post generated!")

                    # Display the post in a structured format
                    sections = new_post.split("\n\n")

                    # Display title
                    if sections[0].startswith("Title:"):
                        st.header(sections[0].replace("Title:", "").strip())
                        sections = sections[1:]

                    # Create an expander for the full post
                    with st.expander("View Generated Post", expanded=True):
                        # Display content sections
                        for section in sections:
                            if section.strip().startswith("#"):
                                st.write("---")
                                st.write("**Hashtags:**")
                                st.write(section)
                            else:
                                st.write(section)

                        # Add copy button
                        if st.button("Copy to Clipboard"):
                            st.code(new_post, language=None)
                            st.info(
                                "Post copied to clipboard! You can now paste it directly to LinkedIn."
                            )

        except Exception as e:
            st.error(f"Error in post generator: {str(e)}")

    def run(self):
        """Run the Streamlit application."""
        try:
            st.title("LinkedIn Post Generator 📝")
            st.write("Explore existing posts or generate new ones!")

            st.sidebar.title("Navigation")
            page = st.sidebar.radio("Go to", ["Existing Posts", "Generate New Post"])

            if page == "Existing Posts":
                self.show_existing_posts()
            else:
                self.show_post_generator()

            # Add footer
            st.sidebar.markdown("---")
            st.sidebar.markdown("### About")
            st.sidebar.info(
                "This application helps you generate professional "
                "LinkedIn posts about AI and technology using the Groq API. "
                "The generated posts are structured similarly to the existing "
                "posts in the database."
            )
        except Exception as e:
            st.error(f"Error in run method: {str(e)}")
