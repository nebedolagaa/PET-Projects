# MindStack Blog Platform

A modern, terminal-inspired blog application built with Node.js and Express.js. This project demonstrates full-stack web development skills with a sleek, professional design reminiscent of a hacker terminal.

![MindStack Demo](https://img.shields.io/badge/Status-Online-brightgreen)
![Node.js](https://img.shields.io/badge/Node.js-v18+-green)
![Express.js](https://img.shields.io/badge/Express.js-v5.1.0-blue)
![Progressive Web App](https://img.shields.io/badge/PWA-Ready-purple)

## 🚀 Live Demo

Visit the live application: [MindStack Blog](http://localhost:3000)

## 📷 Screenshots

### Main Dashboard
- Clean, terminal-inspired interface
- Responsive card layout with hover effects
- Pagination system for better navigation

### Features Overview
- Create, Read, Update, Delete (CRUD) operations
- Progressive Web App (PWA) capabilities
- Mobile-responsive design
- Terminal-themed UI with modern touches

## 🛠️ Technologies Used

### Backend
- **Node.js** - Runtime environment
- **Express.js** - Web framework
- **EJS** - Template engine for dynamic HTML
- **Body-parser** - Middleware for parsing request bodies
- **Method-override** - HTTP method override middleware

### Frontend
- **Bootstrap 5.3.0** - CSS framework for responsive design
- **Bootstrap Icons** - Icon library
- **Custom CSS** - Terminal-inspired styling with modern animations

### PWA Features
- **Web App Manifest** - For installable app experience
- **Service Worker Ready** - Offline capability support
- **Responsive Icons** - Multiple favicon sizes for all devices

## 🎯 Learning Objectives

This project was created to reinforce and practice key web development concepts:

- **Server-side rendering** with EJS templates
- **RESTful API design** with Express.js routing
- **CRUD operations** without database persistence
- **Responsive web design** with Bootstrap
- **Progressive Web App** development
- **Modern JavaScript** (ES6+ modules)
- **Git version control** and project structure
- **Web performance optimization**

## 📁 Project Structure

```
MindStack-Blog/
├── app.js                 # Main application file
├── package.json          # Dependencies and scripts
├── README.md            # Project documentation
├── public/              # Static files
│   ├── styles.css       # Custom CSS styling
│   ├── favicon.ico      # Website icon
│   ├── site.webmanifest # PWA manifest
│   └── icons/           # App icons for different devices
└── views/               # EJS templates
    ├── index.ejs        # Main blog page
    ├── new.ejs          # Create new post
    ├── edit.ejs         # Edit existing post
    └── view.ejs         # View single post
```

## 🚀 Installation & Setup

### Prerequisites
- Node.js (v18 or higher)
- npm (Node Package Manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/nebedolagaa/mindstack-blog.git
cd mindstack-blog
```

### Step 2: Install Dependencies
```bash
npm install
```

### Step 3: Start the Application
```bash
npm start
```

### Step 4: Open in Browser
Navigate to `http://localhost:3000`

## 📝 Usage

### Creating a New Post
1. Click the `[ new_post ]` button
2. Fill in the title and content
3. Click `[ SUBMIT ]` to create

### Editing a Post
1. Click `[ EDIT ]` on any post card
2. Modify the content
3. Click `[ UPDATE ]` to save changes

### Deleting a Post
1. Click `[ DELETE ]` on any post card
2. Confirm the deletion

### Navigation
- Use pagination controls at the bottom
- 6 posts per page for optimal viewing
- Responsive design works on all devices

## 🎨 Design Features

### Terminal-Inspired Theme
- Dark background with neon blue accents
- Monospace fonts for authentic terminal feel
- Smooth hover effects and transitions
- Professional color scheme

### Modern UI Elements
- Gradient buttons with smooth animations
- Card-based layout with subtle shadows
- Responsive navigation bar
- Clean typography hierarchy

### Progressive Web App
- Installable on mobile and desktop
- Offline-ready architecture
- App-like experience with manifest
- Multiple icon sizes for all devices

## 🔧 Technical Implementation

### Server Configuration
```javascript
// Express.js setup with middleware
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(methodOverride('_method'));
```

### Pagination System
```javascript
// Efficient pagination with 6 posts per page
const postsPerPage = 6;
const totalPages = Math.ceil(totalPosts / postsPerPage);
```

### RESTful Routes
- `GET /` - Display all posts with pagination
- `GET /posts/:id` - View single post
- `GET /new` - Show create form
- `POST /posts` - Create new post
- `GET /edit/:id` - Show edit form
- `PUT /posts/:id` - Update existing post
- `DELETE /posts/:id` - Delete post

## 🌟 Key Features

### ✅ CRUD Operations
Complete Create, Read, Update, Delete functionality

### ✅ Responsive Design
Works perfectly on desktop, tablet, and mobile

### ✅ PWA Ready
Installable as a native app experience

### ✅ Modern Styling
Terminal-inspired design with smooth animations

### ✅ Pagination
Efficient navigation through multiple posts

### ✅ Error Handling
Graceful error management and user feedback

## 🔄 Future Enhancements

- [ ] Database integration (MongoDB/PostgreSQL)
- [ ] User authentication and authorization
- [ ] Comment system for posts
- [ ] Search functionality
- [ ] Categories and tags
- [ ] Rich text editor
- [ ] Image upload support
- [ ] Social media sharing

## 📱 Browser Compatibility

- Chrome 60+ ✅
- Firefox 55+ ✅
- Safari 11+ ✅
- Edge 79+ ✅
- Mobile browsers ✅

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the ISC License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**nebedolagaa**
- GitHub: [@nebedolagaa](https://github.com/nebedolagaa)
- Project Link: [MindStack Blog](https://github.com/nebedolagaa/mindstack-blog)

## 🙏 Acknowledgments

- Bootstrap team for the excellent CSS framework
- Express.js community for comprehensive documentation
- Node.js ecosystem for powerful development tools
- Web development community for inspiration and best practices

---

⭐ If you found this project helpful, please give it a star!

Built with 💙 by nebedolagaa
