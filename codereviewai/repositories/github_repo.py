import httpx
import os


async def github_get_repo(repo_link: str) -> str:
    try:
        async with httpx.AsyncClient() as client:
            owner, project_name = repo_link.split("/")[-2:-1][0], repo_link.split("/")[-1].replace(".git", "")
            api_url = f"https://api.github.com/repos/{owner}/{project_name}/contents/"
            headers = {
                "Authorization": f"Bearer {str(os.getenv("GITHUB_TOKEN"))}",
                "Accept": "application/vnd.github.v3+json"
            }
            repo = await client.get(api_url, headers=headers)

            if repo.status_code == 200:
                contents = repo.json()
                result = []

                async def process_item(item):
                    if item['type'] == 'file':
                        if item['name'] == '__init__.py':
                            pass
                        else:
                            file_url = item['download_url']
                            file_response = await client.get(file_url)

                            if file_response.status_code == 200:
                                file_content = file_response.text
                                result.append({
                                    'file': item['name'],
                                    'content': file_content
                                })
                            else:
                                result.append({
                                    'file': item['name'],
                                    'error': 'Failed to download file'
                                })
                    elif item['type'] == 'dir':
                        if item['name'] == '__pycache__':
                            pass
                        else:
                            dir_url = item['url']
                            dir_response = await client.get(dir_url, headers=headers)

                            if dir_response.status_code == 200:
                                dir_contents = dir_response.json()
                                for sub_item in dir_contents:
                                    await process_item(sub_item)

                for item in contents:
                    await process_item(item)

                return result
            else:
                print(repo.status_code)
    except httpx.RequestError as e:
        # raise None
        print(f"httpx.RequestError: {e}")
    except httpx.NetworkError as e:
        # raise None
        print(f"httpx.NetworkError: {e}")