# Calculator App - Frontend

🧮 **Professional Calculator App** optimized for Vercel deployment with modern frontend technologies.

## 🚀 Live Demo

Visit the live app: [Calculator App on Vercel](https://your-calculator-app.vercel.app)

## ✨ Features

- **9 Mathematical Operations**: Addition, Subtraction, Multiplication, Division, Power, Modulo, Percentage, Square Root, Factorial
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Local Storage**: Calculation history persists between sessions
- **Modern UI**: Beautiful gradient design with smooth animations
- **Error Handling**: Comprehensive validation and user-friendly error messages
- **Keyboard Support**: Press Enter to calculate
- **Optimized Performance**: Fast, lightweight, and SEO-friendly

## 🛠️ Technologies Used

- **HTML5**: Semantic markup and accessibility
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript ES6+**: Client-side calculator logic and DOM manipulation
- **Local Storage API**: Persistent calculation history
- **Vercel**: Static site hosting and deployment

## 📁 Project Structure

```
calculator-app/
├── public/
│   └── index.html          # Main frontend application
├── src/                    # Python backend (for Docker/local dev)
├── docker/                 # Docker configuration
├── jenkins/               # CI/CD pipeline configuration
├── package.json           # Node.js configuration
├── vercel.json           # Vercel deployment settings
└── README.md             # Project documentation
```

## 🚀 Quick Start

### Deploy to Vercel (Recommended)

1. **Fork this repository** to your GitHub account
2. **Connect to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your forked repository
   - Deploy automatically!

### Local Development

```bash
# Clone the repository
git clone https://github.com/your-username/calculator-app.git
cd calculator-app

# Serve locally (Python)
python -m http.server 8000 --directory public

# Or use any static file server
npx serve public
```

Visit `http://localhost:8000` to see the app.

## 🎯 Usage

1. **Select Operation**: Choose from 9 mathematical operations
2. **Enter Numbers**: Input values in the form fields
3. **Calculate**: Click "Calculate" or press Enter
4. **View History**: See your recent calculations
5. **Clear History**: Reset calculation history

### Supported Operations

| Operation | Symbol | Example |
|-----------|---------|---------|
| Addition | + | 5 + 3 = 8 |
| Subtraction | - | 10 - 4 = 6 |
| Multiplication | × | 7 × 6 = 42 |
| Division | ÷ | 15 ÷ 3 = 5 |
| Power | ^ | 2 ^ 3 = 8 |
| Modulo | % | 10 % 3 = 1 |
| Percentage | % of | 20% of 50 = 10 |
| Square Root | √ | √16 = 4 |
| Factorial | ! | 5! = 120 |

## 🔧 Configuration

### Vercel Deployment

The `vercel.json` file configures:
- Static file serving from `/public`
- Routing configuration
- Environment variables

### Package.json Scripts

- `npm run dev`: Start local development server
- `npm run build`: Build for production
- `npm run deploy`: Deploy to Vercel

## 🌟 Advanced Features

- **Error Handling**: Division by zero, negative square roots, large factorials
- **Input Validation**: Ensures valid numeric inputs
- **Responsive Design**: Mobile-first approach
- **Accessibility**: ARIA labels and keyboard navigation
- **Performance**: Optimized for fast loading and smooth interactions

## 🧪 Testing

The app includes comprehensive error handling for:
- Invalid inputs
- Mathematical errors (division by zero, etc.)
- Edge cases (very large numbers, negative inputs)

## 📱 Browser Support

- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Mobile browsers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Abdul Naseer Ahmani**
- GitHub: [@anrahmani007](https://github.com/anrahmani007)
- Email: your-email@example.com

## 🙏 Acknowledgments

- Built with modern web technologies
- Optimized for Vercel deployment
- Part of a comprehensive DevOps learning project
- Includes Docker containerization and Jenkins CI/CD pipeline

---

### 🚀 Ready for Production

This calculator app is production-ready with:
- ⚡ Fast loading times
- 📱 Mobile responsiveness  
- 🔒 Client-side security
- 💾 Persistent storage
- 🎨 Modern UI/UX
- 🛠️ Easy deployment

**Deploy now and start calculating!** 🧮
