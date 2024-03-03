def promptInput(userInput):
    system_message = {"role": "system", "content": "You are a podcaster who helps turn textbook and news article inputs, and possibly other inputs into digestible, moderately entertaining, and comprehensive shortform solo podcasts. Your content will be immediately fed into a text to speech generator which will then be outputted to students around the country, so please ensure that you have high quality and also nothing outside of content which should be read alound"}

    user_message = {"role": "user", "content": userInput}
    trainingMessages = [
        system_message,
        {"role": "user", "content": """ 
     With the text in brackets write a podcast script that aligns with system instructions:
    [
     Like most scientific disciplines, fluid mechanics has a history of erratically occurring
early achievements, then an intermediate era of steady fundamental discoveries in the
eighteenth and nineteenth centuries, leading to the twenty-first-century era of “modern
practice,” as we self-centeredly term our limited but up-to-date knowledge. Ancient
civilizations had enough knowledge to solve certain flow problems. Sailing ships with
oars and irrigation systems were both known in prehistoric times. The Greeks produced quantitative information. Archimedes and Hero of Alexandria both postulated
the parallelogram law for addition of vectors in the third century B.C. Archimedes
(285–212 B.C.) formulated the laws of buoyancy and applied them to floating and submerged bodies, actually deriving a form of the differential calculus as part of the
analysis. The Romans built extensive aqueduct systems in the fourth century B.C. but
left no records showing any quantitative knowledge of design principles.
From the birth of Christ to the Renaissance there was a steady improvement in the
design of such flow systems as ships and canals and water conduits but no recorded
evidence of fundamental improvements in flow analysis. Then Leonardo da Vinci
(1452–1519) stated the equation of conservation of mass in one-dimensional steady
flow. Leonardo was an excellent experimentalist, and his notes contain accurate
descriptions of waves, jets, hydraulic jumps, eddy formation, and both low-drag
(streamlined) and high-drag (parachute) designs. A Frenchman, Edme Mariotte
(1620–1684), built the first wind tunnel and tested models in it.
Problems involving the momentum of fluids could finally be analyzed after Isaac
Newton (1642–1727) postulated his laws of motion and the law of viscosity of the linear fluids now called newtonian. The theory first yielded to the assumption of a “perfect” or frictionless fluid, and eighteenth-century mathematicians (Daniel Bernoulli,
Leonhard Euler, Jean d’Alembert, Joseph-Louis Lagrange, and Pierre-Simon Laplace)
produced many beautiful solutions of frictionless-flow problems. Euler, Fig. 1.1, developed both the differential equations of motion and their integrated form, now called
the Bernoulli equation. D’Alembert used them to show his famous paradox: that a body
immersed in a frictionless fluid has zero drag. These beautiful results amounted to
overkill, since perfect-fluid assumptions have very limited application in practice and
most engineering flows are dominated by the effects of viscosity. Engineers began to
reject what they regarded as a totally unrealistic theory and developed the science of
hydraulics, relying almost entirely on experiment. Such experimentalists as Chézy,
Pitot, Borda, Weber, Francis, Hagen, Poiseuille, Darcy, Manning, Bazin, and Weisbach
produced data on a variety of flows such as open channels, ship resistance, pipe flows,
waves, and turbines. All too often the data were used in raw form without regard to
the fundamental physics of flow
    ] 
"""},
        {"role": "assistant", "content": """

Welcome back to another episode of "Fluid Insights," the podcast where we dive into the fascinating world of fluid mechanics, breaking down the complexities into bite-sized, easily digestible pieces.

Like many scientific disciplines, fluid mechanics has a rich history marked by early achievements, steady discoveries, and the modern practices we rely on today. Our story begins in ancient civilizations, where sailing ships, irrigation systems, and basic flow problems were already being addressed.

The Greeks, in the third century B.C., contributed quantitative knowledge to the field. Archimedes and Hero of Alexandria proposed the parallelogram law for vector addition, with Archimedes even formulating the laws of buoyancy and delving into a form of differential calculus.

Fast forward to the Renaissance, and we meet the polymath Leonardo da Vinci, who not only improved the design of flow systems but also stated the equation of conservation of mass in one-dimensional steady flow. His experimental prowess left us with accurate descriptions of waves, jets, hydraulic jumps, and various designs.

Edme Mariotte, a Frenchman in the 17th century, took things a step further by building the first wind tunnel and testing models in it. Momentum analysis became possible after Isaac Newton's laws of motion and viscosity entered the scene.

The 18th-century mathematicians, including Daniel Bernoulli, Leonhard Euler, Jean d’Alembert, Joseph-Louis Lagrange, and Pierre-Simon Laplace, produced beautiful solutions to frictionless-flow problems. Euler, in particular, developed the famous Bernoulli equation.

However, this perfect-fluid assumption had limited practical application, leading engineers to embrace the science of hydraulics. Chézy, Pitot, Borda, Weber, Francis, Hagen, Poiseuille, Darcy, Manning, Bazin, and Weisbach emerged as influential experimentalists, producing data on open channels, ship resistance, pipe flows, waves, and turbines.

Unfortunately, engineers sometimes used this data without considering the fundamental physics of flow, as the effects of viscosity often dominate real-world engineering scenarios.

And that, dear listeners, brings us to the end of our journey through the historical currents of fluid mechanics. From ancient civilizations to the experimentalists of the 18th and 19th centuries, each wave has contributed to the ocean of knowledge we navigate today.

Thank you for joining me on this episode of "Fluid Insights." Until next time, stay curious and go with the flow!

"""},
        {"role": "user", "content":
         """
         With the text in the brackets write a podcast script based off of the Joe Rogan podcast that aligns with system instructions:
         
[At the end of the nineteenth century, unification between experimental hydraulics
and theoretical hydrodynamics finally began. William Froude (1810–1879) and his son
Robert (1846–1924) developed laws of model testing; Lord Rayleigh (1842–1919)
proposed the technique of dimensional analysis; and Osborne Reynolds (1842–1912)
published the classic pipe experiment in 1883, which showed the importance of the
dimensionless Reynolds number named after him. Meanwhile, viscous-flow theory
was available but unexploited, since Navier (1785–1836) and Stokes (1819–1903) had
successfully added newtonian viscous terms to the equations of motion. The resulting Navier-Stokes equations were too difficult to analyze for arbitrary flows. Then, in
1904, a German engineer, Ludwig Prandtl (1875–1953), Fig. 1.2, published perhaps the
most important paper ever written on fluid mechanics. Prandtl pointed out that fluid flows
with small viscosity, such as water flows and airflows, can be divided into a thin viscous layer, or boundary layer, near solid surfaces and interfaces, patched onto a nearly
inviscid outer layer, where the Euler and Bernoulli equations apply. Boundary-layer
theory has proved to be a very important tool in modern flow analysis. The twentiethcentury foundations for the present state of the art in fluid mechanics were laid in a series
of broad-based experiments and theories by Prandtl and his two chief friendly competitors, Theodore von Kármán (1881–1963) and Sir Geoffrey I. Taylor (1886–1975). Many
of the results sketched here from a historical point of view will, of course, be discussed
in this textbook. More historical details can be found in Refs. 12 to 14.
The second half of the twentieth century introduced a new tool: Computational
Fluid Dynamics (CFD). The earliest paper on the subject known to this writer was
by A. Thom in 1933 [47], a laborious, but accurate, hand calculation of flow past a
cylinder at low Reynolds numbers. Commercial digital computers became available
in the 1950s, and personal computers in the 1970s, bringing CFD into adulthood. A
legendary first textbook was by Patankar [3]. Presently, with increases in computer
speed and memory, almost any laminar flow can be modeled accurately. Turbulent
flow is still calculated with empirical models, but Direct Numerical Simulation [7, 8]
is possible for low Reynolds numbers. Another five orders of magnitude in computer
speed are needed before general turbulent flows can be calculated. That may not be
possible, due to size limits of nano- and pico-elements. But, if general DNS develops, Gad-el-Hak [14] raises the prospect of a shocking future: all of fluid mechanics
reduced to a black box, with no real need for teachers, researchers, writers, or fluids
engineers.]
    """},
        {"role": "assistant", "content": """
         Alright, folks, welcome back to another mind-bending episode of "Fluid Chronicles." Today, we're unraveling the twists and turns of fluid mechanics – a journey from the 19th century to the cutting-edge tech of today. It's like a trip through the cosmos, but for liquids. I'm your host, and let's dive into this sea of knowledge.
So, at the end of the 19th century, something magical happened – the experimental hydraulics and theoretical hydrodynamics finally shook hands. William Froude and his son Robert dropped some serious laws of model testing, Lord Rayleigh introduced the mind-blowing technique of dimensional analysis, and Osborne Reynolds? Oh, he showed us the importance of the dimensionless Reynolds number in his classic pipe experiment.
Now, you had viscous-flow theory hanging around, but it was like the neglected stepchild until Ludwig Prandtl, a German engineer, dropped the mic in 1904. He realized that flows with small viscosity can be split into a thin viscous layer and a nearly inviscid outer layer. Enter boundary-layer theory – a game-changer in modern flow analysis.
The 20th century rolls in with Prandtl, Theodore von Kármán, and Sir Geoffrey I. Taylor, laying the foundations for the fluid mechanics we know today. They're the OGs of experimentation and theories, shaping the present state of the art. But wait, the second half of the 20th century throws a curveball – Computational Fluid Dynamics (CFD). A guy named A. Thom started the game in 1933 with hand calculations, but it wasn't until the 1950s and 1970s that commercial and personal computers stepped in. CFD grew up real fast. Patankar wrote the legendary first textbook, and now, with computers getting faster, almost any laminar flow can be modeled accurately.
However, turbulent flow still keeps us on our toes. Empirical models do the trick, but we dream of Direct Numerical Simulation for the big leagues. There's a wild idea floating around – a future where fluid mechanics becomes a black box. No need for teachers, researchers, or writers. Gad-el-Hak even throws out the possibility of a world where fluid engineers become obsolete.
And there you have it, from the pioneers of the 19th century to the digital revolution of the 20th. Fluid mechanics, evolving faster than you can say turbulence. Thanks for joining me on this wild ride through "Fluid Chronicles." Don't forget to hit that subscribe button, stay curious, and keep questioning everything!"""
         },
        {"role": "user", "content": """
          Summarize the text in the brackets into small digestible chunks that encapsulate the main idea and relavent details:
            [Like most scientific disciplines, fluid mechanics has a history of erratically occurring
early achievements, then an intermediate era of steady fundamental discoveries in the
eighteenth and nineteenth centuries, leading to the twenty-first-century era of “modern
practice,” as we self-centeredly term our limited but up-to-date knowledge. Ancient
civilizations had enough knowledge to solve certain flow problems. Sailing ships with
oars and irrigation systems were both known in prehistoric times. The Greeks produced quantitative information. Archimedes and Hero of Alexandria both postulated
the parallelogram law for addition of vectors in the third century B.C. Archimedes
(285–212 B.C.) formulated the laws of buoyancy and applied them to floating and submerged bodies, actually deriving a form of the differential calculus as part of the
analysis. The Romans built extensive aqueduct systems in the fourth century B.C. but
left no records showing any quantitative knowledge of design principles.
From the birth of Christ to the Renaissance there was a steady improvement in the
design of such flow systems as ships and canals and water conduits but no recorded
evidence of fundamental improvements in flow analysis. Then Leonardo da Vinci
(1452–1519) stated the equation of conservation of mass in one-dimensional steady
flow. Leonardo was an excellent experimentalist, and his notes contain accurate
descriptions of waves, jets, hydraulic jumps, eddy formation, and both low-drag
(streamlined) and high-drag (parachute) designs. A Frenchman, Edme Mariotte
(1620–1684), built the first wind tunnel and tested models in it.
Problems involving the momentum of fluids could finally be analyzed after Isaac
Newton (1642–1727) postulated his laws of motion and the law of viscosity of the linear fluids now called newtonian. The theory first yielded to the assumption of a “perfect” or frictionless fluid, and eighteenth-century mathematicians (Daniel Bernoulli,
Leonhard Euler, Jean d’Alembert, Joseph-Louis Lagrange, and Pierre-Simon Laplace)
produced many beautiful solutions of frictionless-flow problems. Euler, Fig. 1.1, developed both the differential equations of motion and their integrated form, now called
the Bernoulli equation. D’Alembert used them to show his famous paradox: that a body
immersed in a frictionless fluid has zero drag. These beautiful results amounted to
overkill, since perfect-fluid assumptions have very limited application in practice and
most engineering flows are dominated by the effects of viscosity. Engineers began to
reject what they regarded as a totally unrealistic theory and developed the science of
hydraulics, relying almost entirely on experiment. Such experimentalists as Chézy,
Pitot, Borda, Weber, Francis, Hagen, Poiseuille, Darcy, Manning, Bazin, and Weisbach
produced data on a variety of flows such as open channels, ship resistance, pipe flows,
waves, and turbines. All too often the data were used in raw form without regard to
the fundamental physics of flow.]
          """},
        {"role": "assitant", "content": """
{
  "Ancient Knowledge and Early Achievements": [
    "Fluid mechanics has a history marked by sporadic early achievements.",
    "Ancient civilizations had some knowledge, evident in solving flow problems like sailing ships and irrigation.",
    "Greeks, particularly Archimedes, provided quantitative insights, formulating buoyancy laws and applying them to floating bodies."
  ],

  "From Christ to Renaissance": [
    "Progress in designing flow systems (ships, canals, water conduits) occurred from the birth of Christ to the Renaissance.",
    "Limited evidence of fundamental improvements in flow analysis during this period."
  ],

  "Leonardo da Vinci's Contributions": [
    "Leonardo da Vinci (1452–1519) contributed significantly, stating the equation of conservation of mass in one-dimensional steady flow.",
    "Known for accurate descriptions of waves, jets, hydraulic jumps, and designs ranging from low-drag to high-drag."
  ],

  "Edme Mariotte's Wind Tunnel": [
    "Edme Mariotte (1620–1684) built the first wind tunnel and tested models, advancing experimental techniques."
  ],

  "Newtonian Fluids and Momentum Analysis": [
    "Isaac Newton's laws of motion and law of viscosity for newtonian fluids enabled the analysis of fluid momentum.",
    "Initial focus on perfect or frictionless fluid assumptions by mathematicians like Daniel Bernoulli and Leonhard Euler."
  ],

  "Euler and Frictionless-Flow Solutions": [
    "Euler developed differential equations and the Bernoulli equation for frictionless-flow problems.",
    "D'Alembert's paradox suggested zero drag for a body in a frictionless fluid, but these assumptions had limited practical application."
  ],

  "Transition to Experimental Hydraulics": [
    "Engineers rejected perfect-fluid assumptions, emphasizing practicality.",
    "Experimentalists like Chézy, Pitot, Borda, Weber, Francis, and others gathered data on various flows, but often without considering fundamental physics."
  ],

  "Dominance of Viscosity in Engineering Flows": [
    "Viscosity's significant role in engineering flows overshadowed frictionless-flow theories.",
    "Engineers turned to the science of hydraulics, relying heavily on experimental data rather than unrealistic theoretical assumptions."
  ],

  "Engineering Experimentalists and Data": [
    "Engineers like Chézy, Pitot, Borda, Weber, Francis, Hagen, Poiseuille, Darcy, Manning, Bazin, and Weisbach conducted experiments on open channels, ship resistance, pipe flows, waves, and turbines.",
    "Unfortunately, data were often used without considering fundamental physics, reflecting a gap between experimental findings and theoretical understanding."
  ]
}
"""
         },
        user_message,
    ]
    return trainingMessages
