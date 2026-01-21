import Section from "./Section";

export default function ProblemSection() {
  return (
    <Section id="problem" title="The problem">
      <p>
        Modern prompts combine XML-like tags with Markdown content. Every
        frontier lab recommends this hybrid format. But best practices keep
        evolving as Anthropic, OpenAI, and Google DeepMind update their
        guidance.
      </p>
      <p>
        The challenge isn&apos;t the format—it&apos;s the uncertainty. Should
        you use <code>&lt;instructions&gt;</code> or{" "}
        <code>&lt;task&gt;</code>? Do tags need closing? Can you nest them? The
        answers depend on which model you&apos;re targeting and when you last
        checked the docs.
      </p>
      <p>
        Agent prompt synthesizes evolving guidance from frontier labs into a
        single, living reference—so you can write prompts with confidence.
      </p>
    </Section>
  );
}
