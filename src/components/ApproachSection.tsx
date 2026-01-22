import Section from "./Section";

export default function ApproachSection() {
  return (
    <Section id="approach" title="Why we don't benchmark">
      <p>
        We don&apos;t validate whether XML-tagged prompts outperform pure Markdown empirically. Here&apos;s why:
      </p>

      <p>
        Our goal is{" "}
        <strong>enduring guidance</strong>—advice that remains valid as models improve. The only durable foundation is
        what frontier labs recommend, which also reflects what they use in training.
      </p>

      <p>
        Empirical validation with today&apos;s SOTA models would mean making decisions about the future based on the
        past. When Anthropic, OpenAI, or Google update their guidance, we update ours.
      </p>
    </Section>
  );
}
