# Django Application Security Configuration

## HTTPS and SSL

- All HTTP requests are redirected to HTTPS using `SECURE_SSL_REDIRECT = True`.
- HSTS is configured to enforce HTTPS for one year: `SECURE_HSTS_SECONDS = 31536000`.
- Subdomains are also protected and preloaded for HSTS.

## Secure Cookies

- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` ensure cookies are sent only over HTTPS.

## Secure Headers

- `X_FRAME_OPTIONS = 'DENY'` prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF` prevents MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER` enables browser-based XSS filtering.

## Deployment (Nginx)

- HTTPS enabled using SSL certificates (Let's Encrypt or manually).
- HTTP redirected to HTTPS at the server level.
- `SECURE_PROXY_SSL_HEADER` set for secure forwarding behind a proxy.

## Recommendations

- Regularly renew and monitor SSL certificates.
- Consider adding Content Security Policy (CSP) headers.
- Use tools like [Mozilla Observatory](https://observatory.mozilla.org/) or [SecurityHeaders.com](https://securityheaders.com/) to test your implementation.
