---
author: "Suyog Garg"
title: "LaTeX for Astrophysics PhDs"
date: "2026-05-19"
tags:
    - latex
    - cheatsheet
    - guide
---

**Disclaimer:** Based on ChatGPT 5.5-Pro prompts!

<!--# The Ultimate LaTeX Stack for Astrophysics PhDs-->

> A comprehensive guide and printable cheatsheet for `siunitx`, `physics2`, `acronym`, and advanced paper write-ups.

---

## Recommended Preamble Setup

Copy and paste this snippet into your `.tex` root or `.sty` file. It configures the modular packages, overrides command conflicts, and defines standard astronomy constants (including the stubborn CGS units the community refuses to drop).

```latex
% --- Core Math & Layout 
\usepackage{mathtools}       \% Extends amsmath, improves spacing 
\usepackage{bm}              \% True bold formatting for vectors/tensors (\bm{\alpha}) 
\usepackage{microtype}       \% Subtle typographic adjustments to fix text "rivers"

% --- The Physics Stack
\usepackage{siunitx}        \% Numbers, units, and ranges 
\usepackage{physics2}       \% Modern, bug-free physics shorthand 
\usephysicsmodule{ab, braket, diagmatrix} \% Load specific modules

% --- Specialized Tools ---
\usepackage[printonlyused]{acronym} % Jargon tracking and glossary linking
\usepackage[capitalise]{cleveref}   % Automated smart referencing (e.g., "Eq. (1)")
\usepackage{mhchem}          % Flawless isotope and reaction formatting
\usepackage{booktabs}        % Professional-grade table lines (\toprule, etc.)

% --- Astro-Specific Unit Declarations
\DeclareSIUnit\parsec{pc} 
\DeclareSIUnit\lightyear{ly} 
\DeclareSIUnit\Msol{M_\odot} \% Solar mass 
\DeclareSIUnit\Rsol{R_\odot} \% Solar radius 
\DeclareSIUnit\Lsol{L_\odot} \% Solar luminosity 
\DeclareSIUnit\year{yr} 
\DeclareSIUnit\erg{erg}      \% CGS energy unit 
\DeclareSIUnit\gauss{G}      \% CGS magnetic field strength
```

---

## Expanded Printable Cheatsheet

### 1. `siunitx` (Quantities, Ranges & Formats)

*Tip: If `\qty` conflicts with bracket modules, use `\quantity` explicitly.*


| Output | Code | Description |
| :--- | :--- | :--- |
| $1.23 \text{ kg}$ | `\qty{1.23}{\kg}` | Standard quantity |
| $3.00 \times 10^{8} \text{ m s}^{-1}$ | `\qty{3.00e8}{\m\per\s}` | Scientific notation |
| $\text{g cm}^{-3}$ | `\unit{\g\per\cubic\cm}` | Standalone unit expression |
| $10 \text{ to } 20 \text{ pc}$ | `\qtyrange{10}{20}{\parsec}` | Worded range |
| $1.5 \pm 0.2 \text{ M}_\odot$ | `\qty{1.5(2)}{\Msol}` | Error bounds (short format) |
| $(5.2 \pm 0.1) \times 10^{3} \text{ yr}$ | `\qty{5.2(1)e3}{\year}` | Error with exponent |
| $1\text{, } 2\text{, and } 3 \text{ kpc}$ | `\qtylist{1;2;3}{\kilo\parsec}` | Automated itemized list |
| $45^\circ$ | `\ang{45}` | Degree angle |
| $12^\circ 3' 4''$ | `\ang{12;3;4}` | Arcminutes and arcseconds |

---

### 2. Calculus, Integrals & Brackets (`physics2`)

*Calculus shortcuts in `physics2` require loading the standard engine tools. Always use `\diff` or `\dd` setups for proper spacing around differential operators.*


| Output | Code | Description |
| :--- | :--- | :--- |
| $(x)$ | `\ab(x)` | Automatic scaling parentheses |
| $[x]$ | `\ab[x]` | Automatic scaling square brackets |
| $\{x\}$ | `\ab\{x\}` | Automatic scaling curly braces |
| $\frac{\mathrm{d}y}{\mathrm{d}x}$ | `\frac{\mathrm{d}y}{\mathrm{d}x}` | Standard derivative |
| $\frac{\partial f}{\partial x}$ | `\frac{\partial f}{\partial x}` | Partial derivative |
| $\frac{\partial^2 f}{\partial x^2}$ | `\frac{\partial^2 f}{\partial x^2}` | Second-order partial |
| $\int f(x) \, \mathrm{d}x$ | `\int f(x) \, \mathrm{d}x` | Fixed-space regular integral |
| $\iint \rho \, \mathrm{d}x \, \mathrm{d}y$ | `\iint \rho \, \mathrm{d}x \, \mathrm{d}y` | Double integral space |

---

### 3. Bra-Ket Vector Notation (`physics2`)

*Requires `\usephysicsmodule{braket}`.*


| Output | Code | Description |
| :--- | :--- | :--- |
| $\langle \psi \vert$ | `\bra{\psi}` | Bra vector |
| $\vert \psi \rangle$ | `\ket{\psi}` | Ket vector |
| $\langle \phi \vert \psi \rangle$ | `\braket{\phi}{\psi}` | Inner product |
| $\langle \phi \vert \hat{H} \vert \psi \rangle$ | `\braket{\phi}{\hat{H}}{\psi}` | Matrix elements / Expectation |

---

### 4. `acronym` (Jargon Automation)

**Preamble/Setup Definition Block:**

```latex
\(\begin{acronym}[SMBH] \% Option sets the width margin to match the longest key     \acro{AGN}{Active Galactic Nucleus}     \acro{CMB}{Cosmic Microwave Background}     \acro{ISM}{Interstellar Medium}     \acro{SMBH}{Supermassive Black Hole} \end{acronym} \%\%\)MAGIT_PARSER_PROTECT%%
```

**Document Body Usage Rules:**


| Command | Output (First Use) | Output (Subsequent Uses) | Target Use Case |
| :--- | :--- | :--- | :--- |
| `\ac{AGN}` | Active Galactic Nucleus (AGN) | AGN | Default choice |
| `\acp{AGN}` | Active Galactic Nuclei (AGNs) | AGNs | Plural variants |
| `\acf{AGN}` | Active Galactic Nucleus (AGN) | Active Galactic Nucleus (AGN) | Force full print |
| `\acl{AGN}` | Active Galactic Nucleus | Active Galactic Nucleus | Force long text only |
| `\acs{AGN}` | AGN | AGN | Force abbreviation |

---

## Essential Thesis Packages for Astrophysics Write-ups

### `cleveref` (Smart cross-referencing)

Stop manually typing `Figure~\ref{...}`. If you shift a table to an appendix, `cleveref` changes the text word automatically.

*   `\cref{fig:m87}` $\rightarrow$ `fig. 1`
*   `\Cref{fig:m87}` $\rightarrow$ `Figure 1` (Capitalized automatically at the start of a sentence)
*   `\cref{eq:rad,eq:conv,eq:cond}` $\rightarrow$ `eqs. (1) to (3)` (Automated grouping/sorting)

### `mhchem` (Nucleosynthesis & Astrochemistry)

Perfect for stellar interiors, chemical evolution, and dust modeling.

*   `\ce{^12C(\alpha, \gamma)^16O}` $\rightarrow$ $^{12}\text{C}(\alpha, \gamma)^{16}\text{O}$
*   `\ce{H2O}` $\rightarrow$ $\text{H}_2\text{O}$
*   `\ce{Fe+}` $\rightarrow$ $\text{Fe}^+$

### `booktabs` (High-Impact Data Tables)

Standard LaTeX tables look cheap due to grid layouts. Clear tables use clean spacing.

*   **Rule:** Never use vertical rules (`|`). Use the clear boundary dividers.

```latex
\(\begin{table}[ht] \centering \begin{tabular}{lcc}     \toprule\)
    Cluster Name & Redshift (\(z\)) & Mass (\(\unit{\Msol}\)) \\
    \midrule
    Abell 1689   & 0.183          & \(1.5 \times 10^{15}\) \\
    Bullet Cl.   & 0.296          & \(2.1 \times 10^{15}\) \(\\     \bottomrule \end{tabular} \end{table} \%\%\)MAGIT_PARSER_PROTECT%%
```
