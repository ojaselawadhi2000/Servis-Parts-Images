import os

# ==== CHANGE THESE ====
USERNAME = "ojas-elawadhi"       # your GitHub username
REPO = "servis-parts-images"       # your repo name
ASSETS_FOLDER = "./Assets"              # keep as "./" if script is inside the repo folder
# =====================

base_url = f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO}@main/"
output_lines = []

# Loop through all subfolders (part folders)
for part_folder in os.listdir(ASSETS_FOLDER):
    folder_path = os.path.join(ASSETS_FOLDER, part_folder)
    if os.path.isdir(folder_path):
        output_lines.append(f"=== {part_folder} ===")  # category header
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith((".jpg", ".jpeg", ".png", ".gif")):
                    relative_path = os.path.relpath(os.path.join(root, file), ".")
                    cdn_link = base_url + relative_path.replace("\\", "/")
                    output_lines.append(cdn_link)
        output_lines.append("")  # empty line between categories

# Save all links to a file
with open("cdn_links.txt", "w") as f:
    f.write("\n".join(output_lines))

print("✅ All CDN links saved to cdn_links.txt")