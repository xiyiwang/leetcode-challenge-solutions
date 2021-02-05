# LeetCode Challenge: Simplify Path (02/05/2021)

#   Given a string path, which is an absolute path (starting 
#   with a slash '/') to a file or directory in a Unix-style 
#   file system, convert it to the simplified canonical path. 
# 
#   In a Unix-style file system, a period '.' refers to the 
#   current directory, a double period '..' refers to the 
#   directory up a level, and any multiple consecutive slashes 
#   (i.e. '//') are treated as a single slash '/'. For this 
#   problem, any other format of periods such as '...' are 
#   treated as file/directory names. 
# 
#   The canonical path should have the following format: 
#   * The path starts with a single slash '/'. 
#   * Any two directories are separated by a single slash '/'. 
#   * The path does not end with a trailing '/'. 
#   * The path only contains the directories on the path from 
#     the root directory to the target file or directory (i.e., 
#     no period '.' or double period '..') 
# 
#   Return the simplified canonical path. 
# 
#   Constraints:
#   * 1 <= path.length <= 3000
#   * path consists of English letters, digits, period '.', 
#     slash '/' or '_'. 
#   * path is a valid absolute Unix path.

#   Submission Detail:
#   * Runtime: 32 ms (better than 73.53% of python3 submissions)
#   * Memory Usage: 14.5 MB

def simplifyPath(path: str) -> str:
    stack = []
    file_name = ""
    for c in path + "/":
        if c == "/":
            if file_name == ".":
                file_name = ""
            elif file_name == "..":
                if stack:
                    stack.pop()
                file_name = ""
            else:
                if file_name: 
                    stack.append(file_name)
                    file_name = ""
        else:
            file_name += c
    return "/" + "/".join(stack)

# An even simpler solution using str.split():
def simplifyPath2(path: str) -> str:
    stack = []
    for elem in path.split("/"):
        if stack and elem == "..": stack.pop()
        elif elem not in ['.', '..', '']: stack.append(elem)
    return "/" + "/".join(stack)