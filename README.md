# modal-metabase

Deploy metabase on Modal. Bring your data vis and analytics closer to your ML infra.

![](/assets/Screenshot%202025-01-27%20at%209.59.26 PM.png)

> [!WARNING]
> This deployment isn't tuned for production workloads. Use it as a proof of concept.
> You should provision a separate database like postgres for example and set [environment variables](https://www.metabase.com/docs/latest/installation-and-operation/running-the-metabase-jar-file) appropriately to provision the database and make connections to store whatever data you need to. Metabase supports a [wide range](https://www.metabase.com/docs/latest/databases/connecting) of datastores, making it a great choice for data vis that complements your data eng/ ML work running on Modal.

## Running the demo

1. Clone this repository
    ```sh
    git clone https://github.com/anthonycorletti/modal-metabase.git && cd modal-metabase
    ```
1. Install `uv` if you haven't already: https://docs.astral.sh/uv/getting-started/installation/
1. Install dependencies and activate the virtual environment
    ```sh
    bin/install
    source .venv/bin/activate
    ```
1. Deploy!
    ```sh
    bin/deploy-modal
    ```
1. Visit the deployed app `https://YOUR_MODAL_PROFILE--modal-metabase-metabase.modal.run` and follow the instructions for setting up your metabase!
