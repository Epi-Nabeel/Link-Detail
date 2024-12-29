# LinkDetail

LinkDetail is a Python tool designed to trace the redirection paths of URLs and display the details of each redirection step. This is especially useful for developers, SEO professionals, or anyone needing to debug URL redirects.

## Features
- **Trace Redirect Chains**: Displays each redirection step, including status codes and URLs.
- **Final Destination**: Shows the final URL after all redirects.
- **Error Handling**: Gracefully handles missing or invalid URLs.
- **Lightweight and Simple**: A compact tool that requires minimal dependencies.

## Installation
### Prerequisites
- Python 3.7 or higher
- `requests` library (Install with pip if not already installed)

### Installation Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/Epi-Nabeel/Link-Detail.git
    cd link-detail
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the script:
    ```bash
    python linkdetail.py
    ```
2. Enter the URL you want to trace when prompted, e.g., `http://example.com`.
3. The tool will output:
   - Each redirection step (status code, source URL, and destination URL).
   - The final destination URL.

## Example Output
```
L     III  N   N  K  K       DDD   EEEE  TTTTTT   AA   III  L    
L      I   NN  N  K K        D  D  E       TT    A  A   I   L    
L      I   N N N  KK    ---  D  D  EEE     TT    AAAA   I   L    
L      I   N  NN  K K        D  D  E       TT    A  A   I   L    
LLLL  III  N   N  K  K       DDD   EEEE    TT    A  A  III  LLLL

Version: 1.1
Created by: Epi-Nabeel
https://github.com/Epi-Nabeel

```

## Contributing
Contributions are welcome! If you have ideas for improvements or new features:
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Epi-Nabeel/Epi-Nabeel/blob/main/LICENSE) file for details.

## Author
Created by **Epi-Nabeel**  
GitHub: [Epi-Nabeel](https://github.com/Epi-Nabeel)

---
### Disclaimer
This tool is for educational and debugging purposes. Please use it responsibly and ensure you have permission before tracing URLs.

