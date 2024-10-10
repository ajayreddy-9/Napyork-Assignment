import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('github_dataset.csv')
# Replacing NULL values with 'Unknown' for languages
data['language'].fillna('Unknown', inplace=True)
#title
st.title("GitHub Repositories Data Dashboard") 
#splitting the username and respository_name from repositories
data["username"]=data.repositories.str.split("/").str[0]
data["repository_name"]=data.repositories.str.split("/").str[1]
st.write("Dataset Preview:")
st.dataframe(data.head())
#dropping the repositories
data=data.drop(["repositories"],axis=1)
# Display dataset overview
st.write("Dataset Preview after droping repositories and adding username and repository_name:")
st.dataframe(data.head())



# 1. Top 10 Popular languages on Github 
st.write("### 1. Top 10 Popular languages on Github")
language_counts = data['language'].value_counts()
top_10_languages = language_counts.head(10).sort_values(ascending=True)
plt.figure(figsize=(10, 8))
plt.barh(top_10_languages.index, top_10_languages.values, color='#20b0cf', edgecolor='#0e4551')
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
plt.xlabel('Count', fontsize=16)
plt.ylabel('Language', fontsize=16)
plt.grid()
st.pyplot(plt)

# 2. Top 10 Most contributed repositories on Github 
st.write("### 2. Top 10 Contributed Repositories on Github")
top_10_contributed = data.nlargest(10, 'contributors')
plt.figure(figsize=(10, 6)) 
top_10_contributed.set_index('repository_name')['contributors'].plot(kind='bar', color='#f39c12') 
plt.xlabel('Repository Name', fontweight='bold', labelpad=10)
plt.ylabel('Number of Contributors', fontweight='bold', labelpad=10)
plt.xticks(rotation = 45, ha = 'right')
plt.grid()
st.pyplot(plt)

# 3. Top Repositories by Open Issues
st.write("### 3. Top 10 Repositories by Issues Count on Github")
top_10_issues = data.nlargest(10, 'issues_count')
plt.figure(figsize=(10, 6))
top_10_issues.set_index('repository_name')['issues_count'].plot(kind='bar', color='#9b59b6')
plt.xlabel('Repository Name', fontweight='bold', labelpad=10)
plt.ylabel('Number of Issues', fontweight='bold', labelpad=10)
plt.title('Top 10 Repositories by Issues Count', fontsize=16)
plt.grid()
st.pyplot(plt)


# Subheader for the plot
st.write("### 4. Top 10 Updated Repositories on Github")
top_10_updated = data.nlargest(10, 'pull_requests')
plt.figure(figsize=(10, 6))
top_10_updated.set_index('repository_name')['pull_requests'].plot(kind='bar', color='#e74c3c')
plt.xlabel('Repository Name', fontweight='bold', labelpad=10)
plt.ylabel('Number of Pull Requests', fontweight='bold', labelpad=10)
plt.title('Top 10 Updated Repositories (Pull Requests)', fontsize=16)
plt.grid()
st.pyplot(plt)

# 5. Most Forked Repositories
st.write("### Top 10 Forked Repositories on Github")
top_10_forked = data.nlargest(10, 'forks_count')
plt.figure(figsize=(10, 6))
top_10_forked.set_index('repository_name')['forks_count'].plot(kind='bar', color='#2ecc71')
plt.xlabel('Repository Name', fontweight='bold', labelpad=10)
plt.ylabel('Number of Forks', fontweight='bold', labelpad=10)
plt.title('Top 10 Forked Repositories', fontsize=16)
plt.grid()
st.pyplot(plt)
# 6. Box and Whiskers graph for forks count for each language
st.write("### 6. Box and Whiskers graph for forks count for each language")
sns.set_style("whitegrid")
forks_count_box = sns.catplot(data=data, kind='box', y='language', x='forks_count', height=20, palette='rocket')
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.ylabel('Language', fontsize=20)
plt.xlabel('Forks Count', fontsize=20)
st.pyplot(plt)

# 7. Box and Whiskers graph for issues count for each language
st.write("### 7. Box and Whiskers graph for issues count for each language")
sns.set_style("whitegrid")
issues_count_box = sns.catplot(data=data, kind='box', y='language', x='issues_count', height=20, palette='rocket')
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.ylabel('Language', fontsize=20)
plt.xlabel('Issues Count', fontsize=20)
st.pyplot(plt)

# 8. Box and Whiskers graph for pull requests count for each language
st.write("### 8. Box and Whiskers graph for pull requests count for each language")
sns.set_style("whitegrid")
pull_requests_box = sns.catplot(data=data, kind='box', y='language', x='pull_requests', height=20, palette='rocket')
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.ylabel('Language', fontsize=20)
plt.xlabel('Pull Requests', fontsize=20)
st.pyplot(plt)

# 9. Box and Whiskers graph for contributors count for each language
st.write("### 9. Box and Whiskers graph for contributors count for each language")
sns.set_style("whitegrid")
contributors_box = sns.catplot(data=data, kind='box', y='language', x='contributors', height=20, palette='rocket')
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.ylabel('Language', fontsize=20)
plt.xlabel('Contributors', fontsize=20)
st.pyplot(plt)
