# Squad-Utils

Reusable utility scripts and components shared across the Squad team.

## 📁 Folder & File Structure

Organize reusable code under a **parent category folder** that describes its context or integration.
Example:

```
google/
├── update_google_sheet.py
```

### 🧱 Code Rules

* Each `.py` file should contain **only one function or class**.
* That function/class should be **focused on doing one thing only** (Single Responsibility Principle).

### 📝 Documentation Rules

* If the function/class is **simple**, include a **usage example** as a comment inside the `.py` file.
* If the function/class is **complex**, create a `README.md` inside the same folder explaining:

  * What it does
  * How to use it
  * Any configuration required

## 🚀 Contributing Guidelines

1. **Clone** the repository:

   ```bash
   git clone https://github.com/ziadwaelai/Squad-Utils.git
   ```

2. **Create a new branch** with a descriptive feature name:

   ```bash
   git checkout -b feature/my-awesome-utility
   ```

3. Add your utility under the correct category folder or create a new one.

4. Follow the **code and documentation rules** above.

5. **Push your branch**:

   ```bash
   git push origin feature/my-awesome-utility
   ```

6. **Open a Pull Request**. The repo maintainer will review your code quickly. If it follows the standards, it will be approved easily.

7. **Merge** your branch into the main branch once approved.