import ApproachSection from "@/components/ApproachSection";
import Footer from "@/components/Footer";
import FormatSection from "@/components/FormatSection";
import Hero from "@/components/Hero";
import ToolingSection from "@/components/ToolingSection";
import WhatAgentsWantSection from "@/components/WhatAgentsWantSection";

export default function Home() {
  return (
    <main className="min-h-screen">
      <Hero />
      <WhatAgentsWantSection />
      <FormatSection />
      <ApproachSection />
      <ToolingSection />
      <Footer />
    </main>
  );
}
