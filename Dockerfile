# Step 1: Build with a safe Node.js version
FROM node:18.16.0 AS builder

WORKDIR /app

COPY . .

# Optional: ensure clean environment
RUN rm -rf node_modules package-lock.json && npm install

# Build Vite app
RUN npm run build

# Step 2: Serve with Nginx
FROM nginx:stable-alpine

# Copy built assets
COPY --from=builder /app/dist /usr/share/nginx/html

# Optional: Add custom Nginx config for SPA routing
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
