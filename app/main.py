import time
from modal import App, Image, web_server

name = "modal-metabase"
app = App(name=name)
image = (
    Image.debian_slim()
    .pip_install("requests")
    .env({"MB_JETTY_HOST": "0.0.0.0", "MB_JETTY_PORT": "3000"})
    .run_commands(
        "apt-get update -y",
        "apt-get install -y curl default-jre",
        "curl -L -o /root/metabase.jar https://downloads.metabase.com/latest/metabase.jar",
    )
)


@app.function(
    name="metabase",
    image=image,
    timeout=60 * 15,
    concurrency_limit=100,
    allow_concurrent_inputs=100,
    cpu="2",
    memory="4Gi",
)
@web_server(port=3000)
def metabase() -> None:
    import subprocess
    import requests

    while True:
        try:
            res = requests.get("http://0.0.0.0:3000/")
            if res.status_code == 200:
                print("metabase started!")
                break
        except Exception:
            if (
                subprocess.Popen.poll(
                    subprocess.Popen("ps aux | grep metabase.jar", shell=True)
                )
                is None
            ):
                print("starting metabase...")
                subprocess.Popen("java -jar /root/metabase.jar", shell=True)
            else:
                print("waiting for metabase to start...")
        time.sleep(60)
