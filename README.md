# Ping Coming Soon - Django Implementation

A responsive "coming soon" landing page built with Django and Tailwind CSS. Features email subscription with validation, custom design system using CSS variables, and mobile-first responsive design. Implementation of Frontend Mentor's Ping Coming Soon challenge.

![Project Preview](screenshot.png)

## 🚀 Features

- ✅ Django form handling with custom validation
- ✅ Tailwind CSS with custom design tokens
- ✅ Responsive design (mobile-first)
- ✅ Accessibility features (ARIA labels, screen reader support)
- ✅ Client-side and server-side email validation
- ✅ Custom CSS properties for consistent theming
- ✅ Interactive hover states and transitions
- ✅ Cross-browser compatibility

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **Frontend**: Tailwind CSS, JavaScript (ES6+)
- **Styling**: Custom CSS properties, Responsive design
- **Validation**: Client-side & Server-side email validation
- **Development**: Django development server, Tailwind CLI

## 📱 Responsive Design

- **Mobile**: 375px and up
- **Tablet**: 768px and up  
- **Desktop**: 1024px and up
- **Large Desktop**: 1280px and up

## 🎨 Design System

### Colors
- **Primary Blue**: #4C7BF3
- **Blue Variants**: #15202A, #C2D3FF
- **Gray Scale**: #969696, #EBEBEB, #FBFCFF
- **Accent**: #FF5466 (Error), #2ECC71 (Success)

### Typography
- **Font Family**: Libre Franklin
- **Presets**: 5 different text presets with varying sizes and weights
- **Responsive**: Scales appropriately across devices

### Spacing
- **Scale**: 0px, 8px, 16px, 24px, 32px, 40px, 48px
- **Consistent**: All components use the spacing scale

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js (for Tailwind CSS)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ping-coming-soon-django.git
   cd ping-coming-soon-django
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install django django-tailwind
   ```

4. **Install Tailwind CSS**
   ```bash
   python manage.py tailwind install
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start development servers**
   ```bash
   # Terminal 1: Django development server
   python manage.py runserver
   
   # Terminal 2: Tailwind CSS watcher
   python manage.py tailwind start
   ```

7. **Visit the application**
   Open your browser and go to `http://127.0.0.1:8000`

## 📁 Project Structure

```
ping_coming_soon/
├── home/                          # Main app
│   ├── templates/home/
│   │   └── home.html             # Main landing page
│   ├── forms.py                  # Email validation form
│   ├── views.py                  # View logic
│   └── urls.py                   # App URLs
├── theme/                        # Tailwind CSS app
│   ├── static_src/src/
│   │   └── styles.css           # Custom CSS with design system
│   └── templates/
│       └── base.html            # Base template
├── ping_coming_soon/            # Project settings
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## ✨ Features Breakdown

### Email Validation
- **Client-side**: Real-time validation with JavaScript
- **Server-side**: Django form validation with custom rules
- **Error Handling**: User-friendly error messages
- **Success Feedback**: Confirmation messages

### Responsive Design
- **Mobile-first**: Optimized for mobile devices
- **Flexible Layouts**: Adapts to all screen sizes
- **Touch-friendly**: Appropriate touch targets

### Accessibility
- **ARIA Labels**: Screen reader support
- **Keyboard Navigation**: Full keyboard accessibility
- **Focus States**: Clear focus indicators
- **Semantic HTML**: Proper HTML structure

## 🎯 Frontend Mentor Challenge

This project is a solution to the [Ping single page coming soon](https://www.frontendmentor.io/challenges/ping-single-page-coming-soon-5cadd051fec04111f7b8da3c) challenge on Frontend Mentor.

### Challenge Requirements ✅
- ✅ View the optimal layout for the site depending on device screen size
- ✅ See hover states for all interactive elements
- ✅ Submit email address and see error state if invalid
- ✅ Responsive design for mobile, tablet, and desktop

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure allowed hosts
- [ ] Set up static files serving
- [ ] Configure database for production
- [ ] Set up email backend for form submissions

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Frontend Mentor](https://www.frontendmentor.io) for the design challenge
- [Tailwind CSS](https://tailwindcss.com) for the utility-first CSS framework
- [Django](https://www.djangoproject.com) for the web framework
- [Libre Franklin](https://fonts.google.com/specimen/Libre+Franklin) font family

## 📞 Contact

Your Name - [@yourusername](https://twitter.com/yourusername) - email@example.com

Project Link: [https://github.com/yourusername/ping-coming-soon-django](https://github.com/yourusername/ping-coming-soon-django)
