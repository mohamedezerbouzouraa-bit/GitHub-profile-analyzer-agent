from urllib.parse import urlparse


def extract_username(url: str):
    parts = urlparse(url).path.strip("/").split("/")
    return parts[0] if parts[0] else None


def safe_repo_sort(repos):
    if not isinstance(repos, list):
        return []

    return sorted(
        [r for r in repos if isinstance(r, dict)],
        key=lambda x: x.get("stargazers_count", 0),
        reverse=True
    )
