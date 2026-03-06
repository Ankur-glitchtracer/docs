# 📚 Documentation Portal Setup

Transform your folder structure into a beautiful, searchable documentation website using `mkdocs-material`.

## 1. Installation
If you haven't already, install the dependencies (configured in `pyproject.toml`):

```bash
pip install mkdocs-material
# OR if using uv/poetry
uv pip install mkdocs-material
```

## 2. Configuration
Create a file named `mkdocs.yml` in the root of your project:

```yaml
site_name: System Design & LLD Patterns
theme:
  name: material
  features:
    - navigation.expand
    - content.code.copy
  palette:
    scheme: slate  # Dark mode
    primary: teal
    accent: purple

nav:
  - Home: LEARNING_PATH.md
  - Design Patterns:
    - Creational:
      - Abstract Factory: design_patterns/creational/abstract_factory/ui_toolkit/PROBLEM.md
      - Builder: design_patterns/creational/builder/custom_pc_builder/PROBLEM.md
      # Add other creational patterns...
    - Structural:
      - Adapter: design_patterns/structural/adapter/format_translator/PROBLEM.md
      # Add other structural patterns...
    - Behavioral:
      - Observer: design_patterns/behavioral/observer/iot_notification_system/PROBLEM.md
      # Add other behavioral patterns...
  - Machine Coding:
    - Games:
      - Snake & Ladder: machine_coding/games/snake_ladder/PROBLEM.md
      # Add other games...
    - Systems:
      - Elevator: machine_coding/systems/elevator/PROBLEM.md
      # Add other systems...
  - Real World Systems:
    - E-Commerce: machine_coding/real_world_systems/e_commerce_order_system/PROBLEM.md
    - Ride Sharing: machine_coding/real_world_systems/ride_sharing_service/PROBLEM.md
    - CI/CD: machine_coding/real_world_systems/ci_cd_pipeline/PROBLEM.md
  - Infrastructure Challenges:
    - Docker Job Scheduler: infrastructure_challenges/dockerized_job_scheduler/PROBLEM.md
    - Redis Rate Limiter: infrastructure_challenges/redis_rate_limiter/PROBLEM.md
    - Socket Chat: infrastructure_challenges/socket_chat_app/PROBLEM.md
```

## 3. Serving the UI
Run the following command to start a local server:

```bash
mkdocs serve
```

Open your browser to `http://127.0.0.1:8000`. You will see a structured, searchable website containing all your problem statements and code documentation.
