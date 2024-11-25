FROM python:3.13-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /backend

# Install the application dependencies.
WORKDIR /backend
RUN uv sync --frozen --no-cache

ENV PATH="/backend/.uv/bin:$PATH"

# Run the application.
CMD ["/backend/.venv/bin/uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0", "--reload"]