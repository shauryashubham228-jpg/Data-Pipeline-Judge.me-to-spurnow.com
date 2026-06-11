import json
import os

def generate_bullets():
    # 1. Load your skills config
    with open(".github/skills-spec.json", "r") as f:
        data = json.load(f)
    
    impact = data["business_impact"]
    comp = data["core_competencies"]
    
    # 2. Programmatically frame high-impact PM bullets based on the data
    bullets = [
        f"* **Productized an automated {data['project_name']}** to solve the problem of {impact['problem'].lower().replace('.','')}, directly enabling seamless cross-platform data enablement.",
        f"* **Architected a robust {comp[0]} feature** that cross-references user data across endpoints, resulting in a **{impact['metrics'].split(',')[0]}** framework prior to marketing campaign delivery.",
        f"* **Designed core technical guardrails around {comp[2]}**, optimizing payload deliveries via an intentional delay to preserve platform stability and eliminate upstream API throttling errors."
    ]
    
    markdown_content = "\n### 📊 Automated PM Resume Bullets (Ready to Copy)\n" + "\n".join(bullets) + "\n"
    
    # 3. Read existing README and append or replace the resume section
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            content = f.read()
        
        # If the section already exists, strip old version to prevent endless appending
        if "### 📊 Automated PM Resume Bullets" in content:
            content = content.split("### 📊 Automated PM Resume Bullets")[0]
            
        new_content = content.strip() + "\n" + markdown_content
    else:
        new_content = "# " + data["project_name"] + "\n" + markdown_content

    with open(readme_path, "w") as f:
        f.write(new_content)
        
    print("✅ Successfully updated README.md with fresh PM resume bullets!")

if __name__ == "__main__":
    generate_bullets()
