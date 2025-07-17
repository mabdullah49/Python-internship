# capstone_planner.py

def generate_capstone_plan():
    project_title = input("Enter Project Title: ")
    objective = input("Enter Project Objective (problem it solves): ")
    
    print("\nEnter Key Features (type 'done' when finished):")
    features = []
    while True:
        feature = input("- ")
        if feature.lower() == 'done':
            break
        features.append(feature)
    
    print("\nEnter Tools/Libraries (comma-separated):")
    tools = input("- ").split(',')
    tools = [tool.strip() for tool in tools]
    
    timeline = input("\nEnter Timeline: ")
    
    print("\nEnter Team Members & Roles (type 'done' when finished):")
    team_roles = []
    while True:
        member = input("- ")
        if member.lower() == 'done':
            break
        team_roles.append(member)

    with open('capstone_idea.md', 'w') as file:
        file.write(f"# Capstone Project Plan\n\n")
        file.write(f"**Project Title:** {project_title}\n\n")
        file.write(f"**Objective:**\n{objective}\n\n")
        
        file.write("**Features:**\n")
        for feat in features:
            file.write(f"- {feat}\n")
        file.write("\n")
        
        file.write("**Tools/Libraries:**\n")
        for tool in tools:
            file.write(f"- {tool}\n")
        file.write("\n")
        
        file.write(f"**Timeline:**\n{timeline}\n\n")
        
        file.write("**Team Members & Roles:**\n")
        for member in team_roles:
            file.write(f"- {member}\n")

    print("\nCapstone plan saved to 'capstone_idea.md'.")

if __name__ == "__main__":
    generate_capstone_plan()
