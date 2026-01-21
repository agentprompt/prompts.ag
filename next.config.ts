import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Force metadata to render in <head> instead of streaming to <body>
  // See: https://github.com/vercel/next.js/issues/79313
  htmlLimitedBots: /.*/,
};

export default nextConfig;
