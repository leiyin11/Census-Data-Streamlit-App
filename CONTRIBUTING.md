# Contributing to Census Data Streamlit App

Thank you for your interest in contributing to the Census Data Streamlit App! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, browser)

### Suggesting Enhancements

We welcome feature requests! Please open an issue with:
- A clear description of the enhancement
- The motivation and use case
- Any implementation ideas (optional)

### Pull Requests

1. **Fork the repository** and create your branch from `main`:
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes**:
   - Write clear, readable code
   - Follow the existing code style
   - Add docstrings to functions
   - Comment complex logic

3. **Test your changes**:
   - Run the app locally to ensure it works
   - Test edge cases
   - Verify Docker builds successfully (if applicable)

4. **Commit your changes**:
   ```bash
   git commit -m "Add amazing feature"
   ```

   Use clear, descriptive commit messages:
   - ✅ "Add county filtering by state"
   - ✅ "Fix unemployment calculation for small counties"
   - ❌ "Update code"
   - ❌ "Fixed stuff"

5. **Push to your fork**:
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request** with:
   - A clear title and description
   - Reference to any related issues
   - Screenshots of UI changes (if applicable)

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Census-Data-Streamlit-App.git
   cd Census-Data-Streamlit-App
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run census_app.py
   ```

## Code Style Guidelines

### Python
- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable names
- Keep functions focused and single-purpose
- Add docstrings to all functions:
  ```python
  def function_name(param1, param2):
      """
      Brief description of what the function does.

      Args:
          param1 (type): Description of param1
          param2 (type): Description of param2

      Returns:
          type: Description of return value
      """
      pass
  ```

### Streamlit
- Use `st.cache_data` for expensive operations
- Provide helpful error messages to users
- Use `st.spinner` for long-running operations
- Keep the UI clean and intuitive

### Data Analysis
- Validate data before processing
- Handle missing values appropriately
- Document data transformations
- Use pandas best practices

## Areas for Contribution

We especially welcome contributions in these areas:

### Features
- Additional census variables/metrics
- State or MSA-level analysis
- Time series comparisons
- Interactive maps
- Data filtering and search
- Export to different formats (Excel, JSON)

### Improvements
- Performance optimizations
- Better error handling
- Unit tests
- Documentation
- Accessibility improvements
- Mobile responsiveness

### Visualizations
- New chart types
- Interactive visualizations
- Custom color schemes
- Improved chart readability

### DevOps
- CI/CD pipelines
- Automated testing
- Deployment scripts
- Docker improvements

## Questions?

Feel free to open an issue with the "question" label if you need help or clarification.

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all.

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment, discrimination, or trolling
- Personal or political attacks
- Publishing others' private information
- Any conduct inappropriate in a professional setting

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉
