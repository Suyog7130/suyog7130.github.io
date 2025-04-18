---
title: "How to use LIGO Data Grid CIT as KAGRA-only Member"
date: 2025-03-14T14:40:21+11:00
draft: false
---

As a member of only the KAGRA collaboration and LIGO, in the LIGO-Virgo-KAGRA or IGWN Consortium, the process of obtaining access to LIGO Data Grid (LDG) clusters is not straight-forward.

- First of all, follow steps from Eric's page [here](https://users.monash.edu.au/~erict/Resources/GettingStartedWithLIGO/) if ya have a LIGO account.

- KAGRA members need to request LDG authentication access using the form available at this link: [https://registry.igwn.org/registry/co_petitions/start/coef:25](https://registry.igwn.org/registry/co_petitions/start/coef:25)

- Once you have filled the LDG access form, you should be able to see an option to add your computer's SSH public key. This option exists in the right-hand side under the heading `Authenticators`.

> If later required, additional SSH public keys can be added to the list of Authenticators, by clicking on the "Manage" button for the associated LDG cluster.

- Create and then upload your computer's public SSH key to the `Authenticators` settings, for the LDG key tab.

- After this, someone at CalTech, or LIGO, needs to manually approve your LDG account request and link your provided  username to your . You will receive a confirmation email once that is approved and a `home` directory with your username has been created.

- If it has been a little while and you still haven't received any confirmation email, it may be worthwhile to open a helpdesk ticket and communicate your concern on the mattermost computing help channel. For help regarding how to open a helpdesk ticket, see: [https://computing.docs.ligo.org/guide/computing-centres/cit/](https://computing.docs.ligo.org/guide/computing-centres/cit/)


Checkout the following Helpdesk Ticket discussions for more details : [git.ligo.org/helpdesk/~/7254](https://git.ligo.org/computing/helpdesk/-/issues/7254)

References:
- [https://computing.docs.ligo.org/guide/computing-centres/ldg/](https://computing.docs.ligo.org/guide/computing-centres/ldg/#account)


