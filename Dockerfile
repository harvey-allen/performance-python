FROM python:3.11-slim AS builder

# Install build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libssl-dev \
    pkg-config \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:$PATH"

# Install Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Set workdir for poetry/requirements handling
WORKDIR /build

# Copy dependency files
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry export -f requirements.txt --without-hashes --without dev | pip install -r /dev/stdin

# Copy entire source code
COPY . .

# Build Rust extension with maturin
WORKDIR /build/processing
RUN pip install maturin && \
    maturin build --release && \
    pip install target/wheels/*.whl

# Final stage
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory for app
WORKDIR /app

# Copy installed Python site-packages and binaries
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy actual Python source code (app folder)
COPY --from=builder /build/app /app

# Set entrypoint
CMD ["python", "main.py"]
