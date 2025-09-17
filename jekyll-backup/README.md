# Australian Math Coach Website

A professional Jekyll website for Australian Math Coach, a mathematics tutoring service.

## Features

- **Professional Design**: Clean, modern layout optimized for a math tutoring business
- **Responsive**: Mobile-friendly design that works on all devices
- **Math Support**: Built-in MathJax support for rendering mathematical equations
- **SEO Optimized**: Proper meta tags, sitemap, and structured data
- **GitHub Pages Ready**: Configured for automatic deployment to GitHub Pages

## Pages

- **Home**: Hero section with key features and math examples
- **About**: Information about the tutoring service and approach
- **Services**: Detailed service offerings and pricing
- **Contact**: Contact form and business information

## Setup and Deployment

### Local Development

1. Install Ruby and Bundler
2. Install dependencies:
   ```bash
   bundle install
   ```
3. Run the development server:
   ```bash
   bundle exec jekyll serve
   ```
4. Open [http://localhost:4000](http://localhost:4000) in your browser

### GitHub Pages Deployment

1. Push your code to the `main` branch
2. GitHub Actions will automatically build and deploy the site
3. The site will be available at `https://yourusername.github.io/amc`

### Custom Domain Setup

To use your custom domain (australianmathcoach.com):

1. Add a `CNAME` file with your domain name
2. Configure your domain's DNS settings to point to GitHub Pages
3. Enable HTTPS in your repository settings

## Customization

### Updating Content

- Edit the markdown files in the root directory for page content
- Modify `_config.yml` for site-wide settings
- Update `assets/css/style.css` for styling changes

### Adding New Pages

1. Create a new `.md` file in the root directory
2. Add front matter with title and description
3. Add navigation links in `_layouts/default.html`

### Math Equations

Use LaTeX syntax for math equations:
- Inline: `$x^2 + y^2 = z^2$`
- Display: `$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$`

## Contact Form

The contact form uses Formspree for handling submissions. To set it up:

1. Sign up at [Formspree](https://formspree.io)
2. Create a new form
3. Update the form action URL in `contact.md`

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.