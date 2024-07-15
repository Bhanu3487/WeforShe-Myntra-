import gradio as gr
import pandas as pd

# Example DataFrame (replace with your actual data loading)
df = pd.DataFrame({
    'Profile Name': ['Profile1', 'Profile2', 'Profile3'],
    'Followers Count': [10000, 20000, 15000],
    'Post Link': ['link1', 'link2', 'link3'],
    'Image URL': ['url1', 'url2', 'url3'],
    'Likes': [500, 800, 600],
    'Comments': [50, 100, 80],
    'Date Posted': ['2024-07-01', '2024-07-02', '2024-07-03']
})

# Function to display top X outfits
def display_top_outfits(x):
    # Sort DataFrame by 'Likes' and select top X rows
    df_sorted = df.sort_values(by='Likes', ascending=False).head(x)
    return df_sorted[['Profile Name', 'Likes', 'Comments', 'Followers Count', 'Date Posted']].to_dict('records')

# Create a Gradio interface using Blocks
with gr.Blocks() as demo:
    # Define a slider for selecting top X outfits
    slider = gr.Slider(minimum=1, maximum=len(df), label="Select number of top outfits")
    
    # Define output components to display top X outfits
    with gr.Tabs() as output_table:
        gr.Textbox(label="Profile Name", type="text")
        gr.Textbox(label="Likes", type="text")
        gr.Textbox(label="Comments", type="text")
        gr.Textbox(label="Followers Count", type="text")
        gr.Textbox(label="Date Posted", type="text")
    
    # Set the release action for the slider

    slider.release(display_top_outfits, inputs=slider, outputs=output_table)

if __name__ == "__main__":
    print("Starting Gradio demo...")
    demo.launch()
