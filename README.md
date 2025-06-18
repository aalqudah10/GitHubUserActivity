# GitHub User Activity Tracker

This Python script fetches and displays recent public activities of any GitHub user using the GitHub Events API.

## 🚀 Overview

The tool retrieves events such as repository creation, push events, pull requests, issues, comments, forks, and more. It's a simple yet effective way to monitor a developer's latest GitHub activity from the command line.

Inspired by: [GitHub User Activity Project on roadmap.sh](https://roadmap.sh/projects/github-user-activity)

## 🔧 Features

- View when a user:
  - Creates or deletes repositories
  - Pushes commits
  - Forks repositories
  - Opens or comments on issues and pull requests
  - Adds members to repos
  - Publishes private repositories
- User-friendly CLI interface with `argparse`
- Handles common API errors (404 and 5xx)

## 🧰 Tech Stack

- Python 3
- `requests` library
- GitHub REST API

## 📦 Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/github-user-activity.git
   cd github-user-activity
   ```
2. Install dependencies:
    ```bash
   pip install requests
   ```
## 🚀 Usage
Run the script from the command line by passing a GitHub username:
```bash
python github_user_activity.py <github_username>
Example:
python github_user_activity.py octocat
```
## 🧪 Example Output
```bash
- Pushed 2 commit(s) to octocat/Hello-World
- Created a repo called octocat/NewProject
- Commented on (Bug in README) in octocat/Hello-World
```
## ❗ Error Handling
404 – Username not found
5xx – GitHub server issues
