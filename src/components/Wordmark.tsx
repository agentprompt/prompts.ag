import Image from "next/image";

type WordmarkProps = {
  className?: string;
  animated?: boolean;
};

export default function Wordmark({ className = "", animated = true }: WordmarkProps) {
  return (
    <div className={`${animated ? "wordmark-glow" : "glow-amber"} ${className}`}>
      <Image
        src="/wordmark-dark.svg"
        alt="agentprompt"
        width={320}
        height={80}
        priority
        className="w-full h-auto max-w-[320px] md:max-w-[400px]"
      />
    </div>
  );
}
