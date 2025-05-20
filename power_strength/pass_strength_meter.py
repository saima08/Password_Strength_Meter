import streamlit as st
import re

# Function to evaluate password strength
def evaluate_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine strength level
    if strength == 5:
        return "Strong", feedback, "🟢"  # Green circle for strong
    elif strength >= 3:
        return "Moderate", feedback, "🟡"  # Yellow circle for moderate
    else:
        return "Weak", feedback, "🔴"  # Red circle for weak

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

# Title and description
st.title("🔐 Password Strength Meter")
st.markdown("Check the strength of your password and get feedback to improve it.")

# Input for password
password = st.text_input("Enter your password:", type="password", placeholder="Type your password here...")

# Evaluate password strength
if password:
    strength, feedback, emoji = evaluate_password_strength(password)

    # Display strength level with emoji
    st.subheader(f"Password Strength: {strength} {emoji}")

    # Display feedback in a more structured way
    if feedback:
        st.warning("**Feedback to improve your password:**")
        for item in feedback:
            st.write(f"- {item}")
    else:
        st.success("Your password is strong and meets all the criteria! 🎉")

# Add a separator
st.markdown("---")

# Footer
st.markdown("Created By Saima")