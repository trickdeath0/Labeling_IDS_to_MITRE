# Labeling_IDS_to_MITRE

## Project Overview

Network Intrusion Detection and Prevention Systems (NIDS), such as Snort, monitor network activity and generate alerts for analysis by security experts. These alerts provide critical information about ongoing attacks and help analysts develop theories about the attackers' methods and objectives. However, building accurate hypotheses requires significant expertise and a deep understanding of cybersecurity, which can be challenging due to the lack of direct integration between Snort and comprehensive Cyber Threat Intelligence (CTI).

This project addresses these challenges by leveraging AI to assist analysts and automate the labeling process. We perform various experiments, utilizing techniques such as Few-shot learning and different model training approaches to enhance the process.

By integrating Large Language Models (LLMs) like Gemini, Claude, and ChatGPT, we gain several advantages:
- **Detailed Explanations:** LLMs provide in-depth explanations for each recommended attack technique, which is particularly useful for novice analysts with limited expertise.
- **Extensive Knowledge Base:** LLMs tap into a vast knowledge repository, including data from the MITRE ATT&CK framework, incident reports, vulnerability data, and details about attack groups.

Additionally, we explore the models' capabilities to create a complete machine learning pipeline, including data cleaning, feature selection, model choice, and data splitting. This comprehensive approach has yielded promising results in the classification task.

## Getting Started

### Prerequisites

- Python 3.x
- Access to LLMs (Gemini, Claude, ChatGPT)
- Snort rules dataset
- MITRE ATT&CK framework reference

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Labeling_IDS_to_MITRE.git
   cd Labeling_IDS_to_MITRE
   ```


## Us
Feel free to connect with us on

<p><a href="https://www.linkedin.com/in/shay-giladi/" rel="nofollow noreferrer"><img src="https://i.sstatic.net/gVE0j.png" alt="linkedin"> Shay Giladi</a> </p>

<p><a href="https://www.linkedin.com/in/shalev-shpolyansky-b54268250/" rel="nofollow noreferrer"><img src="https://i.sstatic.net/gVE0j.png" alt="linkedin"> Shalev Shpolyansky</a> </p>

<p><a href="https://www.linkedin.com/in/raz-moyal-b9445b183/" rel="nofollow noreferrer"><img src="https://i.sstatic.net/gVE0j.png" alt="linkedin"> Raz Moyal</a> </p>

:octocat: [Sapir Sharabi](https://github.com/Saposh1) 

