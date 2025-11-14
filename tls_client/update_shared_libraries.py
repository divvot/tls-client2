import requests

def update_libraries():
    shared_library_version = "1.11.2-4"

    github_download_url = "https://github.com/divvot/tls-client/releases/download/v{}/{}"
    github_repo_filenames = [
        # Windows
        f"tls-client-{shared_library_version}-windows-386.dll",
        f"tls-client-{shared_library_version}-windows-amd64.dll",

        # MacOS
        f"tls-client-{shared_library_version}-darwin-amd64.dylib",
        f"tls-client-{shared_library_version}-darwin-arm64.dylib",
        # Linux
        f"tls-client-{shared_library_version}-linux-amd64.so",
        f"tls-client-{shared_library_version}-linux-386.so",
        f"tls-client-{shared_library_version}-linux-arm64.so"
    ]
    dependency_filenames = [
        # Windows
        "tls-client-32.dll",
        "tls-client-64.dll",
        # MacOS
        "tls-client-arm64.dylib",
        "tls-client-x86.dylib",
        # Linux
        "tls-client-amd64.so",
        "tls-client-x86.so",
        "tls-client-arm64.so"
    ]

    for github_filename, dependency_filename in zip(github_repo_filenames, dependency_filenames):
        url = github_download_url.format(shared_library_version, github_filename)
        print(url)
        response = requests.get(
            url=url
        )

        with open(f"tls_client/dependencies/{dependency_filename}", "wb") as f:
            f.write(response.content)

if __name__ == '__main__':
    update_libraries()
