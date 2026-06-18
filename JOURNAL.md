# 1. Keyboard Layout Planning

> ⏱️ **Time Logged:** 2 Hours

Before starting the electrical design, I spent time deciding on the overall layout of the keyboard. I chose a 75% layout because it balances functionality and desk space well. One challenge was fitting all 75 keys while maintaining comfortable spacing and room for the OLED display. I experimented with several arrangements before settling on the final design. This planning stage helped prevent larger issues later in the project and gave me a clearer idea of how all the components would fit together.

---

# 2. Schematic Design

> ⏱️ **Time Logged:** 4 Hours

I worked on creating the schematic for the keyboard. Compared to smaller projects I had done previously, this design was significantly more complicated because it included 75 switches, a Raspberry Pi Pico, an OLED display, and RGB underglow LEDs.

One challenge I encountered was organizing the keyboard matrix and ensuring every switch was connected correctly. During the design process I ran into several ERC errors caused by missing connections and incorrect net assignments. Rather than trying random fixes, I systematically reviewed each section of the schematic and traced every issue back to its source. After multiple revisions, I was able to eliminate all errors and complete a schematic that was both functional and organized.

---

# 3. PCB Layout & Routing

> ⏱️ **Time Logged:** 6 Hours

I worked on laying out and routing the PCB for the keyboard. This was by far the most time-consuming portion of the project.

With 75 switches, RGB LEDs, the OLED display, and supporting circuitry, routing quickly became challenging due to the large number of connections and limited space available. My initial placement resulted in several congested areas where routing became difficult. To solve this, I repositioned components multiple times and rerouted large portions of the board to improve trace organization.

I also had to carefully consider mounting hole placement and mechanical clearances to ensure traces would not be damaged during assembly. This stage taught me the importance of balancing electrical requirements with mechanical constraints. Overall, I am very happy with how compact and organized the final PCB turned out.

---

# 4. Plate Design

> ⏱️ **Time Logged:** 2 Hours

I designed the keyboard plate that supports all 75 switches. While it seemed straightforward at first, ensuring that every switch cutout was aligned correctly required careful attention to detail.

I spent time verifying measurements against both the PCB and key layout to ensure proper fitment. Since even small alignment errors can affect the assembly process, I double-checked all dimensions before finalizing the design.

---

# 5. Top Case Design

> ⏱️ **Time Logged:** 2 Hours

I created the top case for the keyboard. The primary challenge was integrating the switch openings, OLED display opening, and overall aesthetics while maintaining compatibility with the plate and PCB.

I made several adjustments to dimensions and clearances to ensure components would fit comfortably without interfering with one another. The final design provides support while maintaining a clean appearance.

---

# 6. Bottom Case Design

> ⏱️ **Time Logged:** 2 Hours

I created the bottom case that houses the PCB and internal electronics. Although the design itself was relatively simple, determining the correct dimensions required careful measurement.

I had to account for the thickness of the PCB, standoffs, mounting hardware, and tolerances associated with 3D printing. To reduce the risk of assembly issues, I added additional clearance in several locations where the fit would otherwise have been too tight.

---

# 7. Assembly Creation & Verification

> ⏱️ **Time Logged:** 1.5 Hours

I created a complete assembly model of the keyboard to verify that all components fit together correctly.

During this stage I discovered a few minor alignment issues that were not obvious when viewing individual parts. Being able to identify and correct these problems before manufacturing saved both time and potential cost. The assembly also allowed me to visualize the finished product and confirm that all dimensions were correct.

---

# 8. Firmware Development

> ⏱️ **Time Logged:** 2.5 Hours

I developed the firmware for the keyboard. Since I already had experience with Python, learning the basic structure of the firmware was not difficult. However, configuring the keyboard matrix, OLED display functionality, and RGB lighting required learning several new concepts.

I spent time reading documentation and experimenting with test configurations before implementing the final design. While there was a learning curve at first, I gained a much better understanding of how firmware interacts with hardware systems.

---

# 9. Parts Sourcing

> ⏱️ **Time Logged:** 2 Hours

I sourced all of the components required for the keyboard, including switches, keycaps, LEDs, the Raspberry Pi Pico, display, and assembly hardware.

I originally expected this process to be quick, but I quickly discovered that balancing cost, quality, and availability was more difficult than anticipated. Several components were either out of stock or significantly more expensive than expected. After comparing multiple suppliers and alternatives, I finalized a bill of materials that met both performance and budget requirements.

---

# 10. GitHub Repository & Documentation

> ⏱️ **Time Logged:** 1 Hour

I organized all project files and uploaded them to my GitHub repository. I also created documentation describing the project, design process, and manufacturing files.

Although documentation was one of the final steps, I believe it is an important part of any engineering project because it allows others to understand, reproduce, and improve upon the design in the future.

---

# Total Project Statistics

| Category                         | Time Logged |
| -------------------------------- | ----------: |
| Keyboard Layout Planning         |       2 hrs |
| Schematic Design                 |       4 hrs |
| PCB Layout & Routing             |       6 hrs |
| Plate Design                     |       2 hrs |
| Top Case Design                  |       2 hrs |
| Bottom Case Design               |       2 hrs |
| Assembly Creation & Verification |     1.5 hrs |
| Firmware Development             |     2.5 hrs |
| Parts Sourcing                   |       2 hrs |
| GitHub & Documentation           |        1 hr |
| **Total Time**                   |  **25 hrs** |

---

# Reflection

I am immensely grateful for the opportunity to design and develop a custom keyboard from the ground up. I started this project because I wanted to create something that combined electrical engineering, mechanical design, and software development into a single product that I could personally use.

One of the biggest lessons I learned was that engineering is an iterative process. Whether I was fixing ERC errors, rerouting traces on the PCB, adjusting mechanical tolerances, or learning how to configure firmware features, very few parts of the project worked perfectly on the first attempt. Each challenge required research, experimentation, and multiple revisions before reaching a satisfactory solution.

Throughout the project I became more comfortable using professional design tools and working through technical problems independently. I also gained a deeper understanding of how electrical, mechanical, and software systems interact within a complete product. Most importantly, I was able to transform an initial idea into a fully designed keyboard that I am genuinely proud of. The experience and skills gained throughout this project will be valuable in future engineering projects and have strengthened my interest in hardware design.
