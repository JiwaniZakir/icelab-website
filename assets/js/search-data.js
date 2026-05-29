// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/icelab-website/";
    },
  },{id: "nav-team",
          title: "team",
          description: "Current and former members of the ICE Lab.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/icelab-website/team/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "Active research projects at the ICE Lab.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/icelab-website/projects/";
          },
        },{id: "nav-research",
          title: "research",
          description: "Research areas at the ICE Lab — 3-D ICs, hardware security, and near-threshold circuits.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/icelab-website/research/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "Publications from the ICE Lab at Drexel University.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/icelab-website/publications/";
          },
        },{id: "nav-contact",
          title: "contact",
          description: "Get in touch with the ICE Lab.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/icelab-website/contact/";
          },
        },{id: "nav-news",
          title: "news",
          description: "Latest announcements from the ICE Lab at Drexel University.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/icelab-website/news/";
          },
        },{id: "post-iccd-2025-tutorial-on-machine-learning-for-automated-physical-design",
        
          title: "ICCD 2025 Tutorial on Machine Learning for Automated Physical Design",
        
        description: "Prof. Ioannis Savidis presented an ICCD 2025 tutorial on machine learning for automated physical design.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2025/iccd-2025-ml-tutorial/";
          
        },
      },{id: "post-iscas-2025-tutorial-on-ml-ai-techniques-for-analog-eda",
        
          title: "ISCAS 2025 Tutorial on ML-AI Techniques for Analog EDA",
        
        description: "Prof. Ioannis Savidis presented an ISCAS 2025 tutorial on emerging machine learning techniques for analog EDA.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2025/iscas-2025-ml-ai-tutorial/";
          
        },
      },{id: "post-vaibhav-venugopal-rao-completes-ph-d-on-analog-circuit-security",
        
          title: "Vaibhav Venugopal Rao Completes Ph.D. on Analog Circuit Security",
        
        description: "Vaibhav Venugopal Rao defended his dissertation on enhancing analog circuit security through obfuscation.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2024/vaibhav-rao-phd-defense/";
          
        },
      },{id: "post-tvlsi-paper-on-hidden-costs-of-analog-deobfuscation-attacks",
        
          title: "TVLSI Paper on Hidden Costs of Analog Deobfuscation Attacks",
        
        description: "ICE Lab publication in IEEE TVLSI on security analysis of analog circuit obfuscation.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2023/tvlsi-analog-deobfuscation/";
          
        },
      },{id: "post-two-papers-presented-at-iscas-2019",
        
          title: "Two Papers Presented at ISCAS 2019",
        
        description: "The papers entitled Increasing the SAT Attack Resiliency of In-Cone Logic Locking and Mesh Based Obfuscation of Analog Circuit Properties were presented at ISCA",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2019/two-papers-presented-at-iscas-2019/";
          
        },
      },{id: "post-prof-ioannis-savidis-awarded-2018-nsf-career-award",
        
          title: "Prof. Ioannis Savidis Awarded 2018 NSF CAREER Award",
        
        description: "Prof. Ioannis Savidis has been awarded a prestigious NSF CAREER Award for “Parameter Obfuscation: A Novel Methodology for the Protection of Analog Intellectual",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2018/prof-ioannis-savidis-awarded-2018-nsf-career-award/";
          
        },
      },{id: "post-the-joseph-and-shirley-carleone-endowed-fellowship-is-awarded-to-divy-pathak-for-the-academic-year-2017-2018",
        
          title: "The Joseph and Shirley Carleone Endowed Fellowship is awarded to Divy Pathak for...",
        
        description: "The Joseph and Shirley Carleone Endowed Fellowship for the academic year 2017-2018 is awarded to Divy Pathak by the College of Engineering, Drexel University.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2018/the-joseph-and-shirley-carleone-endowed-fellowship-is-awarde/";
          
        },
      },{id: "post-two-papers-presented-at-gomactech-2018",
        
          title: "Two Papers Presented at GOMACTech 2018",
        
        description: "Prof. Ioannis Savidis presented two ICE Lab papers at the Government Microcircuit Applications &amp; Critical Technology Conference in Miami, Florida held on March",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2018/two-papers-presented-at-gomactech-2018/";
          
        },
      },{id: "post-prof-ioannis-savidis-wins-ieee-philadelphia-section-award",
        
          title: "Prof. Ioannis Savidis Wins IEEE Philadelphia Section Award",
        
        description: "Prof. Ioannis Savidis wins the 2018 IEEE Philadelphia Section Delaware Valley Young Electrical Engineer of the Year Award. Citation: “For contributions in hardw",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2018/ieee-philly_2018award/";
          
        },
      },{id: "post-united-states-patent-number-9-912-325-awarded-on-march-6-2018",
        
          title: "United States Patent Number 9,912,325 awarded on March 6, 2018",
        
        description: "The patent “ Power supply voltage detection and power delivery circuit ” is issued by the USPTO on March 6, 2018 as United States Patent Number 9,912,325. Prof.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2018/united-states-patent-number-9912325-awarded-on-march-6-2018/";
          
        },
      },{id: "post-divy-pathak-receives-the-2017-ieee-circuits-and-systems-pre-doctoral-scholarship",
        
          title: "Divy Pathak receives the 2017 IEEE Circuits and Systems Pre-Doctoral Scholarship",
        
        description: "The 2017 IEEE CASS Pre-Doctoral Scholarship is awarded to Divy Pathak. She received the award at the 2017 IEEE ISCAS conference on May 31, 2017 at Baltimore, MD",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2017/divya-pathak-receives-the-2017-ieee-circuits-and-systems-pre-doctoral-scholarship/";
          
        },
      },{id: "post-allen-rothwarf-scholarship-awarded-to-divy-pathak",
        
          title: "Allen Rothwarf Scholarship awarded to Divy Pathak",
        
        description: "The Allen Rothwarf Scholarship for the academic year 2016-2017 is awarded to Divy Pathak by the Department of Electrical and Computer Engineering, Drexel Univer",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2017/allen-rothwarf-scholarship-awarded-to-divya-pathak/";
          
        },
      },{id: "post-divy-pathak-receives-the-nsf-iredefine-professional-development-award",
        
          title: "Divy Pathak receives the NSF iREDEFINE Professional Development Award",
        
        description: "Divy Pathak is awarded the 2017 National Science Foundation Professional Development Award to participate in the iREDEFINE project.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2017/divya-pathak-receives-the-nsf-iredefine-professional-development-award/";
          
        },
      },{id: "post-papers-presented-at-glsvlsi-2016",
        
          title: "Papers Presented at GLSVLSI 2016",
        
        description: "Kyle Juretus presented “Reduced Overhead Gate Level Logic Encryption” and Prof. Ioannis Savidis presented “Load Balanced On-Chip Power Delivery for Average Curr",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2016/papers-presented-at-glsvlsi-2016/";
          
        },
      },{id: "post-divy-pathak-wins-conference-travel-awards",
        
          title: "Divy Pathak wins conference travel awards",
        
        description: "Divy Pathak is awarded the 2016 IEEE Circuits and Systems Society Student Travel Award and the International Travel Award from Drexel University to present her",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2016/divya-wins-conference-travel-awards/";
          
        },
      },{id: "post-kyle-juretus-awarded-student-fellowship",
        
          title: "Kyle Juretus Awarded Student Fellowship",
        
        description: "Kyle Juretus, a second year Ph.D. student working in my laboratory, was awarded both a Science, Mathematics and Research for Transformation (SMART) Defense Scho",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2016/kyle-juretus-awarded-student-fellowship/";
          
        },
      },{id: "post-papers-presented-at-gomactech-2016",
        
          title: "Papers Presented at GOMACTech 2016",
        
        description: "Two ICE Lab papers were presented at the Government Microcircuit Applications &amp; Critical Technology Conference in Orlando Florida held on March 14-17, 2016: 1)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2016/papers-presented-at-gomactech-2016/";
          
        },
      },{id: "post-paper-presented-at-the-33rd-ieee-international-conference-on-computer-design-iccd",
        
          title: "Paper presented at the 33rd IEEE International Conference on Computer Design (ICCD)",
        
        description: "The paper titled “Realizing Complexity-Effective On-Chip Power Delivery for Many-Core Platforms by Exploiting Optimized Mapping” was presented at the 33rd IEEE",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2015/paper-presented-at-the-33rd-ieee-international-conference-on-computer-design-iccd/";
          
        },
      },{id: "post-paper-presented-at-52nd-design-automation-conference",
        
          title: "Paper presented at 52nd Design Automation Conference",
        
        description: "The paper titled “ElasticCore: Enabling Dynamic Heterogeneity with Joint Core and Voltage/Frequency Scaling” was presented at the 52nd Design Automation Confere",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2015/paper-presented-at-52nd-design-automation-conference/";
          
        },
      },{id: "post-divy-pathak-awarded-the-2015-frank-and-agnes-seaman-fellowship",
        
          title: "Divy Pathak awarded the 2015 Frank and Agnes Seaman Fellowship",
        
        description: "The Frank and Agnes Seaman Fellowship for the academic year 2014-2015 is awarded to Divy Pathak by the Department of Electrical and Computer Engineering, Drexel",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2015/divya-pathak-awarded-the-2015-frank-and-agnes-seaman-fellowship/";
          
        },
      },{id: "post-paper-presented-at-the-ieee-soi-3d-subthreshold-microelectronics-technology-unified-conference-s3s",
        
          title: "Paper presented at the IEEE SOI-3D-Subthreshold Microelectronics Technology Unified Conference (S3S)",
        
        description: "The paper titled “Power Supply Voltage Detection and Clamping Circuit for 3-D Integrated Circuits” was presented at the IEEE SOI-3D-Subthreshold Microelectronic",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2014/paper-presented-at-ieee-soi-3d-subthreshold-microelectronics-technology-unified-conference-s3s/";
          
        },
      },{id: "post-paper-presented-at-the-27th-ieee-international-system-on-chip-conference-socc",
        
          title: "Paper presented at the 27th IEEE International System-on-Chip Conference (SOCC)",
        
        description: "The paper titled “Run-Time Voltage Detection Circuit for 3-D IC Power Delivery” was presented at the 27th IEEE International System-on-Chip Conference (SOCC), h",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/icelab-website/blog/2014/paper-presented-at-the-27th-ieee-international-system-on-chip-conference-socc/";
          
        },
      },{id: "news-we-are-recruiting-phd-students-interested-in-3-d-ics-hardware-security-and-energy-efficient-circuit-design-see-our-contact-page-for-details",
          title: 'We are recruiting PhD students interested in 3-D ICs, hardware security, and energy-efficient...',
          description: "",
          section: "News",},{id: "projects-clock-tree-synthesis-cts-for-3-d-integrated-circuits",
          title: 'Clock Tree Synthesis (CTS) for 3-D Integrated Circuits',
          description: "Recent work has explored CTS for 3-D ICs by extending algorithms devised for 2D ICs such as the Methods of Means and Medians (MMM), Nearest Neighbor Graph (NNG) and Deferred Merging Algorithm (DME) fo...",
          section: "Projects",handler: () => {
              window.location.href = "/icelab-website/projects/3d-cts/";
            },},{id: "projects-3-d-integrated-circuit-power-delivery",
          title: '3-D Integrated Circuit Power Delivery',
          description: "An important issue for 3-D integrated circuits is the design of a robust power distribution network that can provide sufficient current to every load within a system. Power delivery in 3-D integrated ...",
          section: "Projects",handler: () => {
              window.location.href = "/icelab-website/projects/3d-power-delivery/";
            },},{id: "projects-synchronization-in-3-d-integrated-circuits",
          title: 'Synchronization in 3-D Integrated Circuits',
          description: "Synchronization amongst various sequential elements of a two-dimensional IC is a challenge which is further exacerbated when considering a three-dimensional IC. Our work focused on multi-plane synchro...",
          section: "Projects",handler: () => {
              window.location.href = "/icelab-website/projects/3d-synchronization/";
            },},{id: "projects-attack-prevention-through-design-for-trust-algorithms-and-methodologies",
          title: 'Attack Prevention Through Design for Trust Algorithms and Methodologies',
          description: "EDA tools used for circuit design implement algorithms and methodologies that account for the power, area, and performance of the many blocks comprising the IC. With the more recent threat of untruste...",
          section: "Projects",handler: () => {
              window.location.href = "/icelab-website/projects/design-for-trust/";
            },},{id: "projects-run-time-detection-and-countermeasures",
          title: 'Run-time Detection and Countermeasures',
          description: "Current work exploring hardware Trojan detection is concentrated around post fabrication testing of an IC. Test vectors are implemented to &quot;activate&quot; hardware Trojans during the post fabrication test ...",
          section: "Projects",handler: () => {
              window.location.href = "/icelab-website/projects/hardware-trojan-detection/";
            },},{id: "projects-power-reduction-using-ntc-with-cml",
          title: 'Power Reduction using NTC with CML',
          description: "Our primary objective is to design circuits with minimum power consumption and higher energy efficiency. We implement NTC to minimize the power of the circuits. However, using purely near-threshold de...",
          section: "Projects",handler: () => {
              window.location.href = "/icelab-website/projects/ntc-cml/";
            },},{id: "projects-on-chip-power-delivery-with-run-time-voltage-regulator-clustering",
          title: 'On-Chip Power Delivery with Run-Time Voltage Regulator Clustering',
          description: "With the paradigm shift in computing systems from performance oriented design to energy efficiency, there is considerable research effort to optimize the core configuration by reducing the over-provis...",
          section: "Projects",handler: () => {
              window.location.href = "/icelab-website/projects/ocvr-clustering/";
            },},{id: "projects-3-d-integrated-free-space-optical-interconnect-for-multi-core-systems",
          title: '3-D Integrated Free-Space Optical Interconnect for Multi-Core Systems',
          description: "State of the art microprocessors and SoCs experience a degradation in the performance and signal integrity of on-chip metal interconnects with each successive technology generation due to increased re...",
          section: "Projects",handler: () => {
              window.location.href = "/icelab-website/projects/optical-interconnect/";
            },},{id: "projects-thermal-modeling-and-mitigation",
          title: 'Thermal Modeling and Mitigation',
          description: "Two of the most omnipresent and challenging issues in high performance 3-D systems are power delivery and thermal management. The interdependence of these issues is of critical importance to 3-D syste...",
          section: "Projects",handler: () => {
              window.location.href = "/icelab-website/projects/thermal-modeling/";
            },},{id: "projects-tsv-modeling-and-characterization",
          title: 'TSV Modeling and Characterization',
          description: "The critical component of a 3-D IC is the through-silicon via. Our seminal work on the electrical characterization of the TSV resistance, capacitance, and inductance as a function of the diameter, len...",
          section: "Projects",handler: () => {
              window.location.href = "/icelab-website/projects/tsv-modeling/";
            },},{id: "team-alec-aversa",
          title: 'Alec Aversa',
          description: "Ph.D. Student | aja367@drexel.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/alec-aversa/";
            },},{id: "team-amit-varde",
          title: 'Amit Varde',
          description: "Ph.D. Student | avv39@drexel.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/amit-varde/";
            },},{id: "team-ashish-sharma",
          title: 'Ashish Sharma',
          description: "Ph.D. Student | as5463@drexel.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/ashish-sharma/";
            },},{id: "team-dr-divy-pathak",
          title: 'Dr. Divy Pathak',
          description: "Ph.D. | divya.pathak@dragons.drexel.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/divya-pathak/";
            },},{id: "team-ioannis-savidis",
          title: 'Ioannis Savidis',
          description: "Associate Professor | isavidis@coe.drexel.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/ioannis-savidis/";
            },},{id: "team-jeff-wu",
          title: 'Jeff Wu',
          description: "Ph.D. Student | jw3723@drexel.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/jeff-wu/";
            },},{id: "team-prof-kyle-juretus",
          title: 'Prof. Kyle Juretus',
          description: "Assistant Professor, Villanova University | kyle.juretus@villanova.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/kyle-juretus/";
            },},{id: "team-nnaemeka-achebe",
          title: 'Nnaemeka Achebe',
          description: "Ph.D. Student | nma334@drexel.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/nnaemeka-achebe/";
            },},{id: "team-pratik-shrestha",
          title: 'Pratik Shrestha',
          description: "Ph.D. Student | ps937@drexel.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/pratik-shrestha/";
            },},{id: "team-saran-phatharodom",
          title: 'Saran Phatharodom',
          description: "Ph.D. Student",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/saran-phatharodom/";
            },},{id: "team-dr-shazzad-hossain",
          title: 'Dr. Shazzad Hossain',
          description: "Staff Engineer, Qualcomm | msh89@dragons.drexel.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/shazzad-hossain/";
            },},{id: "team-dr-vaibhav-venugopal-rao",
          title: 'Dr. Vaibhav Venugopal Rao',
          description: "Staff Engineer, Kioxia | vaibhavvrao93@gmail.com",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/vaibhav-venugopal-rao/";
            },},{id: "team-ziyi-chen",
          title: 'Ziyi Chen',
          description: "Ph.D. Student | zc372@drexel.edu",
          section: "Team",handler: () => {
              window.location.href = "/icelab-website/team/ziyi-chen/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%69%73%61%76%69%64%69%73@%63%6F%65.%64%72%65%78%65%6C.%65%64%75", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=qe9QgMZUjAMC", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/icelab-website/feed.xml", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
