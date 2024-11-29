# duplex-scan

## Project Description

This project is designed to assist users with scanners that can only scan simplex (one side at a time) using the document feed. With this tool, users can scan a document in two passes:

1. Scan the entire document from the first to the last page.
2. Turn the paper stack and scan from the turned last page back to the turned first page.

The tool will reverse the second PDF and merge them together to create a properly ordered duplex (double-sided) scanned document.

## Build and Run Instructions

### Prerequisites

- Docker
- Docker Compose

### Building the Docker Image

To build the Docker image, navigate to the project directory and run: `docker-compose build`

### Running the Service

To run the service, use the following command: `docker-compose up`

The service will be available at <http://localhost:5000>.

### Accessing the Service

Open your web browser and navigate to <http://localhost:5000>. You will see the PDF Merger UI.

#### Using the UI

1. Odd Pages PDF: Click on the "Choose File" button and select the PDF file that contains the odd pages of your document.
2. Even Pages PDF: Click on the "Choose File" button and select the PDF file that contains the even pages of your document.
3. Click on the "Merge PDFs" button to upload the files and merge them.

Once the merge is complete, a download will be started.

## Linting

To lint your project locally using GitHub Super-Linter, follow these steps:

1. Ensure you have Docker installed on your machine.
2. Run the following command to lint your project: `docker-compose -f docker-compose.lint.yml run --rm lint`
3. To lint and automatically fix issues, run: `docker-compose -f docker-compose.lint.yml run --rm fix`

## Running Tests

To run the tests, use the following command: `pytest`
