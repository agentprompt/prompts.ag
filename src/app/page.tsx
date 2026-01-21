import Hero from "@/components/Hero";
import ProblemSection from "@/components/ProblemSection";
import WhatAgentsWantSection from "@/components/WhatAgentsWantSection";
import FormatSection from "@/components/FormatSection";
import ToolingSection from "@/components/ToolingSection";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <main className="min-h-screen">
      <Hero />
      <ProblemSection />
      <WhatAgentsWantSection />
      <FormatSection />
      <ToolingSection />
      <Footer />
    </main>
  );
}
