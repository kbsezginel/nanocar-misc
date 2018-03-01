"""
Adding, commiting and pushing changes for multiple files (including images) using PyGitHub.
Taken from: https://stackoverflow.com/questions/38594717/how-do-i-push-new-files-to-github
"""
import base64
from github import Github
from github import InputGitTreeElement

token = '5bf1fd927dfb8679496a2e6cf00cbe50c1c87145'
g = Github(token)
repo = g.get_user().get_repo('mathematics')
file_list = [
    'numerical_analysis/regression_analysis/simple_regression_analysis.png',
    'numerical_analysis/regression_analysis/simple_regression_analysis.py'
]
commit_message = 'Add simple regression analysis'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)
element_list = list()
for entry in file_list:
    with open(entry, 'rb') as input_file:
        data = input_file.read()
    if entry.endswith('.png'):
        data = base64.b64encode(data)
    element = InputGitTreeElement(entry, '100644', 'blob', data)
    element_list.append(element)
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)
""" An egregious hack to change the PNG contents after the commit """
for entry in file_list:
    with open(entry, 'rb') as input_file:
        data = input_file.read()
    if entry.endswith('.png'):
        old_file = repo.get_contents(entry)
        commit = repo.update_file('/' + entry, 'Update PNG content', data, old_file.sha)
