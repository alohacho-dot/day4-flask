---
name: Serene Editorial
colors:
  surface: '#fbf9f4'
  surface-dim: '#dbdad5'
  surface-bright: '#fbf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ee'
  surface-container: '#f0eee9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e4e2dd'
  on-surface: '#1b1c19'
  on-surface-variant: '#4d4540'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#7e756f'
  outline-variant: '#cfc4bd'
  surface-tint: '#635d5a'
  primary: '#181512'
  on-primary: '#ffffff'
  primary-container: '#2d2926'
  on-primary-container: '#96908b'
  inverse-primary: '#cdc5c0'
  secondary: '#685d4a'
  on-secondary: '#ffffff'
  secondary-container: '#eddec6'
  on-secondary-container: '#6c614e'
  tertiary: '#18150d'
  on-tertiary: '#ffffff'
  tertiary-container: '#2d2920'
  on-tertiary-container: '#969084'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e9e1dc'
  primary-fixed-dim: '#cdc5c0'
  on-primary-fixed: '#1e1b18'
  on-primary-fixed-variant: '#4b4642'
  secondary-fixed: '#f0e0c9'
  secondary-fixed-dim: '#d3c5ae'
  on-secondary-fixed: '#221a0c'
  on-secondary-fixed-variant: '#4f4534'
  tertiary-fixed: '#eae2d4'
  tertiary-fixed-dim: '#cdc6b8'
  on-tertiary-fixed: '#1e1b13'
  on-tertiary-fixed-variant: '#4b463c'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1120px
  article-max: 720px
  gutter: 24px
  margin-mobile: 20px
  section-gap: 80px
  element-gap: 16px
---

## Brand & Style

The design system is anchored in the concept of "Mindful Reading." It prioritizes the reader's focus by stripping away digital noise, replacing it with a tactile, editorial aesthetic that feels more like a high-end independent magazine than a standard website. The brand personality is intellectual, serene, and welcoming—designed to evoke the feeling of a quiet afternoon in a well-lit library.

The visual style is a blend of **Minimalism** and **Editorial Design**. It leverages heavy whitespace and a restricted color palette to create a sense of luxury through restraint. The design system avoids trendy "app-like" gradients in favor of flat, tonal layering that emphasizes content hierarchy and legibility.

## Colors

The palette for this design system is built on a foundation of "Oatmeal" and "Ink." The primary background is a soft, non-reflective cream (#F9F7F2) to reduce eye strain during long-form reading. 

- **Primary (#2D2926):** A deep, warm charcoal used for high-contrast typography and primary actions. It is softer than pure black, maintaining the organic feel.
- **Secondary (#D6C7B0):** A mid-tone beige used for dividers, secondary buttons, and subtle UI accents.
- **Neutral/Surface (#EBE3D5):** A slightly darker cream used for cards and section backgrounds to create a clear tonal distinction from the main page body.
- **Accent (#8C6A5D):** A muted terracotta used sparingly for text links and hover states to provide a touch of warmth without breaking the minimalist aesthetic.

## Typography

This design system utilizes a sophisticated typographic pairing to balance tradition and modernity. 

**Newsreader** is the primary serif typeface for headlines and long-form article titles. Its classic, literary proportions provide an authoritative yet warm voice. **Plus Jakarta Sans** is used for body text, navigation, and metadata. Its soft, rounded terminals complement the beige palette, ensuring the interface feels modern and approachable.

Line heights are intentionally generous (1.6x to 1.7x for body text) to maximize readability. Metadata and labels should utilize the `label-caps` style to create a distinct visual break from the narrative text.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to ensure optimal line lengths for reading. Content should be centered with significant lateral whitespace.

- **Main Container:** Limited to 1120px for general pages.
- **Article Container:** Constrained to 720px for the reading experience, preventing eye fatigue from excessively long lines of text.
- **Whitespace:** Use "Section Gaps" of 80px or more to separate major content blocks, allowing the layout to breathe.
- **Responsive:** On mobile, margins reduce to 20px, and all multi-column layouts should collapse into a single vertical stack.

## Elevation & Depth

To maintain a clean, professional look, this design system avoids heavy shadows. Depth is communicated through **Tonal Layers** and **Low-contrast Outlines**.

- **Surfaces:** Elements like cards or search bars should use a subtle color shift (e.g., placing a Tertiary colored card on a Neutral background) rather than a shadow.
- **Borders:** Use 1px solid strokes in the Secondary color (#D6C7B0) for buttons and input fields.
- **Interactive States:** When an element is hovered, use a very soft, diffused ambient shadow (4% opacity, 12px blur, tinted with the Primary color) to provide tactile feedback without cluttering the UI.

## Shapes

The shape language is "Softly Geometric." This design system uses a subtle corner radius (4px to 8px) to soften the edges of the UI while maintaining a professional, structured appearance. 

Buttons and input fields should utilize a 4px radius (`rounded-sm`). Featured image containers and cards may use an 8px radius (`rounded-lg`) to differentiate them from functional UI elements. This restrained use of rounding prevents the design from appearing too "bubbly" or informal.

## Components

### Buttons
Primary buttons are solid Primary (#2D2926) with white text. Secondary buttons use a Secondary border with Primary text. All buttons should have generous horizontal padding (24px) and use the `label-caps` typography style.

### Cards
Blog post cards should be minimalist. They consist of a large image with an 8px radius, followed by a `label-caps` category, a `headline-md` title, and a short snippet in `body-md`. Avoid containing cards in boxes; use whitespace to define their boundaries.

### Input Fields
Fields are represented by a single bottom border or a very light 4-sided stroke. Focus states should transition the border color from Secondary to Primary.

### Chips & Tags
Used for article categories. These should be pill-shaped with a Neutral background and `label-caps` text. They are meant to be secondary in the visual hierarchy.

### Navigation
The header should be transparent or match the background, featuring a simple centered logo and text-only navigation items with ample spacing. No borders or shadows should separate the header from the content.