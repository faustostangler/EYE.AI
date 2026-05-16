---
name: Rethinking AI TCO: Why Cost per Token Is the Only Metric That Matters - NVIDIA Blog
keywords: (placeholder)
metadata:
  url: https://blogs.nvidia.com/blog/lowest-token-cost-ai-factories/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Rethinking AI TCO: Why Cost per Token Is the Only Metric That Matters 
Skip to content
Skip to main content ![](data:image/svg+xml,%3csvg id='Logo' xmlns='http://www.w3.org/2000/svg' width='108.472' height='20' viewBox='0 0 108.472 20'%3e %3cpath id='Reg' d='M1072.628,253.918v-.3h.192c.105,0,.248.008.248.136s-.073.163-.2.163h-.243m0,.211h.129l.3.524h.327l-.33-.545a.3.3,0,0,0,.311-.323c0-.285-.2-.377-.53-.377h-.482v1.245h.276v-.524m1.4-.1a1.2,1.2,0,1,0-1.2,1.157,1.14,1.14,0,0,0,1.2-1.157m-.347,0a.854.854,0,0,1-.855.891v0a.889.889,0,1,1,.855-.887Z' transform='translate(-965.557 -237.878)'/%3e %3cpath id='NVIDIA' d='M463.9,151.934v13.127h3.707V151.934Zm-29.164-.018v13.145h3.74v-10.2l2.918.01a2.674,2.674,0,0,1,2.086.724c.586.625.826,1.632.826,3.476v5.995h3.624V157.8c0-5.183-3.3-5.882-6.536-5.882Zm35.134.018v13.127h6.013c3.2,0,4.249-.533,5.38-1.727a7.352,7.352,0,0,0,1.316-4.692,7.789,7.789,0,0,0-1.2-4.516c-1.373-1.833-3.352-2.191-6.306-2.191Zm3.677,2.858h1.594c2.312,0,3.808,1.039,3.808,3.733s-1.5,3.734-3.808,3.734h-1.594Zm-14.992-2.858-3.094,10.4-2.965-10.4h-4l4.234,13.127h5.343l4.267-13.127Zm25.749,13.127h3.708V151.935h-3.709ZM494.7,151.939l-5.177,13.117h3.656l.819-2.318h6.126l.775,2.318h3.969l-5.216-13.118Zm2.407,2.393,2.246,6.145h-4.562Z' transform='translate(-399.551 -148.155)'/%3e %3cpath id='Eye_Mark' data-name='Eye Mark' d='M129.832,124.085v-1.807c.175-.013.353-.022.533-.028,4.941-.155,8.183,4.246,8.183,4.246s-3.5,4.863-7.255,4.863a4.553,4.553,0,0,1-1.461-.234v-5.478c1.924.232,2.31,1.082,3.467,3.01l2.572-2.169a6.81,6.81,0,0,0-5.042-2.462,9.328,9.328,0,0,0-1,.059m0-5.968v2.7c.177-.014.355-.025.533-.032,6.871-.232,11.348,5.635,11.348,5.635s-5.142,6.253-10.5,6.253a7.906,7.906,0,0,1-1.383-.122v1.668a9.1,9.1,0,0,0,1.151.075c4.985,0,8.59-2.546,12.081-5.559.578.463,2.948,1.591,3.435,2.085-3.319,2.778-11.055,5.018-15.44,5.018-.423,0-.829-.026-1.228-.064v2.344h18.947v-20Zm0,13.009v1.424c-4.611-.822-5.89-5.615-5.89-5.615a9.967,9.967,0,0,1,5.89-2.85v1.563h-.007a4.424,4.424,0,0,0-3.437,1.571s.845,3.035,3.444,3.908m-8.189-4.4a11.419,11.419,0,0,1,8.189-4.449v-1.463c-6.043.485-11.277,5.6-11.277,5.6s2.964,8.569,11.277,9.354v-1.555C123.731,133.451,121.643,126.728,121.643,126.728Z' transform='translate(-118.555 -118.117)' fill='%2374b71b'/%3e %3c/svg%3e)
Company Blog
Artificial Intelligence
AI Infrastructure
Physical AI
Gaming & Creating
Industries
Subscribe
![](data:image/svg+xml,%3csvg id='Icon_Search_32px' data-name='Icon Search 32px' xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3e %3cg id='Icon' transform='translate(2.55 2.55)'%3e %3cg id='Ellipse_26' data-name='Ellipse 26' fill='none' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'%3e %3ccircle cx='7.35' cy='7.35' r='7.35' stroke='none'/%3e %3ccircle cx='7.35' cy='7.35' r='6.6' fill='none'/%3e %3c/g%3e %3cline id='Line_8' data-name='Line 8' x2='4.875' y2='4.875' transform='translate(12.45 12.45)' fill='none' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3c/g%3e %3crect id='Container' width='24' height='24' fill='none'/%3e %3c/svg%3e)![](data:image/svg+xml,%3csvg id='Icon_Close_32px' data-name='Icon Close 32px' xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3e %3cline id='Line_3_C' data-name='Line 3 C' y1='5.25' x2='5.25' transform='translate(6.75 12)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cline id='Line_3_C-2' data-name='Line 3 C' x2='5.25' y2='5.25' transform='translate(12 12)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cline id='Line_2_B' data-name='Line 2 B' x2='0.75' transform='translate(11.25 12)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cline id='Line_2_A' data-name='Line 2 A' x2='0.75' transform='translate(12 12)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cline id='Line_1_B' data-name='Line 1 B' x2='5.25' y2='5.25' transform='translate(6.75 6.75)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cline id='Line_1_A' data-name='Line 1 A' y1='5.25' x2='5.25' transform='translate(12 6.75)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='1.5' opacity='0'%3e %3crect width='24' height='24' stroke='none'/%3e %3crect x='0.75' y='0.75' width='22.5' height='22.5' fill='none'/%3e %3c/g%3e %3c/svg%3e)
US Select Location
The Americas![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e)
Argentina
Brasil (Brazil)
Canada
Chile
Colombia
México (Mexico)
Peru
United States
Europe![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e)
België (Belgium)
Belgique (Belgium)
Česká Republika (Czech Republic)
Danmark (Denmark)
Deutschland (Germany)
España (Spain)
France
Italia (Italy)
Nederland (Netherlands)
Norge (Norway)
Österreich (Austria)
Polska (Poland)
România (Romania)
Suomi (Finland)
Sverige (Sweden)
Türkiye (Turkey)
United Kingdom
Rest of Europe
Asia![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e)
Australia
中国大陆 (Mainland China)
India
日本 (Japan)
대한민국 (South Korea)
Singapore
台灣 (Taiwan)
Middle East![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e)
Middle East
Sign In
NVIDIA Account
NVIDIA Store Account ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32'%3e%3cdefs%3e%3cstyle%3e.cls-1%7bopacity:0;%7d.cls-2%7bopacity:0.1;%7d.cls-3%7bfill:%23f0f;%7d.cls-4%7bfill:none;stroke:%23000;stroke-miterlimit:10;stroke-width:2px;%7d%3c/style%3e%3csymbol id='n32-menu' data-name='n32-menu' viewBox='0 0 32 32'%3e%3cg class='cls-1'%3e%3cg class='cls-2'%3e%3cpath class='cls-3' d='M30,2V30H2V2H30m2-2H0V32H32V0Z'/%3e%3c/g%3e%3c/g%3e%3cline class='cls-4' x1='6' y1='10' x2='26' y2='10'/%3e%3cline class='cls-4' x1='6' y1='16' x2='26' y2='16'/%3e%3cline class='cls-4' x1='6' y1='22' x2='26' y2='22'/%3e%3c/symbol%3e%3c/defs%3e%3cg id='Layer_2' data-name='Layer 2'%3e%3cg id='Art_3.0' data-name='Art 3.0'%3e%3cuse width='32' height='32' xlink:href='%23n32-menu'/%3e%3c/g%3e%3c/g%3e%3c/svg%3e)
Company Blog
Subscribe
Artificial Intelligence![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e) Inference  Agentic AI  Open Source  Generative AI  AI for Good  Research 
AI Infrastructure![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e) AI Factory  Cloud  Hardware  Networking  Sovereign AI 
Physical AI![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e) Robotics  Driving  Simulation and Design  Digital Twin  Smart Spaces 
Gaming & Creating![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e) NVIDIA RTX  GeForce NOW  RTX AI Garage  Workstation 
Industries![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e) Healthcare and Life Sciences  Industrial and Manufacturing  Telecommunications  Energy  Financial Services  Retail and CPG  ![](data:image/svg+xml,%3csvg id='Icon_Search_32px' data-name='Icon Search 32px' xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3e %3cg id='Icon' transform='translate(2.55 2.55)'%3e %3cg id='Ellipse_26' data-name='Ellipse 26' fill='none' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'%3e %3ccircle cx='7.35' cy='7.35' r='7.35' stroke='none'/%3e %3ccircle cx='7.35' cy='7.35' r='6.6' fill='none'/%3e %3c/g%3e %3cline id='Line_8' data-name='Line 8' x2='4.875' y2='4.875' transform='translate(12.45 12.45)' fill='none' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3c/g%3e %3crect id='Container' width='24' height='24' fill='none'/%3e %3c/svg%3e) ![](data:image/svg+xml,%3csvg id='Icon_Close_32px' data-name='Icon Close 32px' xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3e %3cline id='Line_3_C' data-name='Line 3 C' y1='5.25' x2='5.25' transform='translate(6.75 12)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cline id='Line_3_C-2' data-name='Line 3 C' x2='5.25' y2='5.25' transform='translate(12 12)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cline id='Line_2_B' data-name='Line 2 B' x2='0.75' transform='translate(11.25 12)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cline id='Line_2_A' data-name='Line 2 A' x2='0.75' transform='translate(12 12)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cline id='Line_1_B' data-name='Line 1 B' x2='5.25' y2='5.25' transform='translate(6.75 6.75)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cline id='Line_1_A' data-name='Line 1 A' y1='5.25' x2='5.25' transform='translate(12 6.75)' fill='%23fff' stroke='%23666' stroke-miterlimit='10' stroke-width='1.5'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='1.5' opacity='0'%3e %3crect width='24' height='24' stroke='none'/%3e %3crect x='0.75' y='0.75' width='22.5' height='22.5' fill='none'/%3e %3c/g%3e %3c/svg%3e) ![](data:image/svg+xml,%3csvg id='Logo' xmlns='http://www.w3.org/2000/svg' width='108.472' height='20' viewBox='0 0 108.472 20'%3e %3cpath id='Reg' d='M1072.628,253.918v-.3h.192c.105,0,.248.008.248.136s-.073.163-.2.163h-.243m0,.211h.129l.3.524h.327l-.33-.545a.3.3,0,0,0,.311-.323c0-.285-.2-.377-.53-.377h-.482v1.245h.276v-.524m1.4-.1a1.2,1.2,0,1,0-1.2,1.157,1.14,1.14,0,0,0,1.2-1.157m-.347,0a.854.854,0,0,1-.855.891v0a.889.889,0,1,1,.855-.887Z' transform='translate(-965.557 -237.878)'/%3e %3cpath id='NVIDIA' d='M463.9,151.934v13.127h3.707V151.934Zm-29.164-.018v13.145h3.74v-10.2l2.918.01a2.674,2.674,0,0,1,2.086.724c.586.625.826,1.632.826,3.476v5.995h3.624V157.8c0-5.183-3.3-5.882-6.536-5.882Zm35.134.018v13.127h6.013c3.2,0,4.249-.533,5.38-1.727a7.352,7.352,0,0,0,1.316-4.692,7.789,7.789,0,0,0-1.2-4.516c-1.373-1.833-3.352-2.191-6.306-2.191Zm3.677,2.858h1.594c2.312,0,3.808,1.039,3.808,3.733s-1.5,3.734-3.808,3.734h-1.594Zm-14.992-2.858-3.094,10.4-2.965-10.4h-4l4.234,13.127h5.343l4.267-13.127Zm25.749,13.127h3.708V151.935h-3.709ZM494.7,151.939l-5.177,13.117h3.656l.819-2.318h6.126l.775,2.318h3.969l-5.216-13.118Zm2.407,2.393,2.246,6.145h-4.562Z' transform='translate(-399.551 -148.155)'/%3e %3cpath id='Eye_Mark' data-name='Eye Mark' d='M129.832,124.085v-1.807c.175-.013.353-.022.533-.028,4.941-.155,8.183,4.246,8.183,4.246s-3.5,4.863-7.255,4.863a4.553,4.553,0,0,1-1.461-.234v-5.478c1.924.232,2.31,1.082,3.467,3.01l2.572-2.169a6.81,6.81,0,0,0-5.042-2.462,9.328,9.328,0,0,0-1,.059m0-5.968v2.7c.177-.014.355-.025.533-.032,6.871-.232,11.348,5.635,11.348,5.635s-5.142,6.253-10.5,6.253a7.906,7.906,0,0,1-1.383-.122v1.668a9.1,9.1,0,0,0,1.151.075c4.985,0,8.59-2.546,12.081-5.559.578.463,2.948,1.591,3.435,2.085-3.319,2.778-11.055,5.018-15.44,5.018-.423,0-.829-.026-1.228-.064v2.344h18.947v-20Zm0,13.009v1.424c-4.611-.822-5.89-5.615-5.89-5.615a9.967,9.967,0,0,1,5.89-2.85v1.563h-.007a4.424,4.424,0,0,0-3.437,1.571s.845,3.035,3.444,3.908m-8.189-4.4a11.419,11.419,0,0,1,8.189-4.449v-1.463c-6.043.485-11.277,5.6-11.277,5.6s2.964,8.569,11.277,9.354v-1.555C123.731,133.451,121.643,126.728,121.643,126.728Z' transform='translate(-118.555 -118.117)' fill='%2374b71b'/%3e %3c/svg%3e)
US
Select Location
The Americas![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e)
Argentina
Brasil (Brazil)
Canada
Chile
Colombia
México (Mexico)
Peru
United States
Europe![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e)
België (Belgium)
Belgique (Belgium)
Česká Republika (Czech Republic)
Danmark (Denmark)
Deutschland (Germany)
España (Spain)
France
Italia (Italy)
Nederland (Netherlands)
Norge (Norway)
Österreich (Austria)
Polska (Poland)
România (Romania)
Suomi (Finland)
Sverige (Sweden)
Türkiye (Turkey)
United Kingdom
Rest of Europe
Asia![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e)
Australia
中国大陆 (Mainland China)
India
日本 (Japan)
대한민국 (South Korea)
Singapore
台灣 (Taiwan)
Middle East![](data:image/svg+xml,%3csvg id='n32-caret-down' xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3e %3cpath id='Line_1a' data-name='Line 1a' d='M1,0,8,7,1,14' transform='translate(22.5 11.5) rotate(90)' fill='none' stroke='%23666' stroke-width='2'/%3e %3cg id='Container' fill='none' stroke='%23666' stroke-width='2' opacity='0'%3e %3crect width='32' height='32' stroke='none'/%3e %3crect x='1' y='1' width='30' height='30' fill='none'/%3e %3c/g%3e %3c/svg%3e)
Middle East
NVIDIA Account
NVIDIA Store Account
Rethinking AI TCO: Why Cost per Token Is the Only Metric That Matters
April 15, 2026 by Shruti Koparkar
0
Share
Share This Article
[X](https://twitter.com/intent/tweet?text=Rethinking AI TCO: Why Cost per Token Is the Only Metric That Matters https%3A%2F%2Fblogs.nvidia.com%2Fblog%2Flowest-token-cost-ai-factories%2F)
Facebook
LinkedIn
Copy link Link copied! 
Traditional data centers only stored, retrieved and processed data. In the generative and agentic AI era, these facilities have evolved into AI token factories. With AI inference becoming their primary workload, their primary output is intelligence manufactured in the form of tokens.
This transformation demands a corresponding shift in how the economics of AI infrastructure, including total cost of ownership (TCO), is assessed. Enterprises evaluating AI infrastructure still too often focus on peak chip specifications, compute cost or floating point operations per second for every dollar spent, aka FLOPS per dollar.
The distinction that matters is this:
Compute cost is what enterprises pay for AI infrastructure, whether rented from cloud providers or owned on premises.
FLOPS per dollar is how much raw computing power an enterprise gets for every dollar spent, but raw compute and real-world token output are not the same thing.
Cost per token is an enterprise's all-in cost to produce each delivered token, usually represented as cost per million tokens.
The first two are merely input metrics. Optimizing for inputs while the business runs on output is a fundamental mismatch.
Cost per token determines whether enterprises can profitably scale AI. It's the one TCO metric that directly accounts for hardware performance, software optimization, ecosystem support and real-world utilization — and NVIDIA delivers the lowest cost per token in the industry.
What Are the Factors That Lower Token Cost?
Understanding how to optimize token cost requires looking at the equation for calculating cost per million tokens. 
In this equation, many enterprises evaluating AI infrastructure focus on the numerator: the cost per GPU per hour. For cloud deployments, this is the hourly rate paid to a cloud provider; for on-premises deployments, it's the effective hourly cost derived from amortizing owned infrastructure. The real key to reducing token cost, however, lies in the denominator: maximizing the delivered token output.
That denominator carries two business implications.
Minimize token cost: When this increase in token output is reflected through the cost equation, it drives down cost per token, which is what grows the profit margin on every interaction served.
Maximize revenue: More tokens delivered per second also translates to more tokens per megawatt, which means more intelligence to use in AI-powered products and services, generating more revenue from the same infrastructure investment.
So focusing only on the numerator means missing what drives the denominator. Think of it as an “inference iceberg”: The numerator sits above the surface, visible and easy to compare. The denominator is everything beneath the surface, which represents key factors that determine real-world token output. Accurately evaluating AI infrastructure starts with asking what lies beneath. 
Surface-level inquiry:
What is the cost per GPU hour?
What are the peak petaflops and high-bandwidth memory capacity?
What are the FLOPS per dollar?
In-depth cost analysis:
What is the cost per million tokens? Specifically, what is the cost per million tokens for large-scale mixture-of-experts (MoE) reasoning models, which represent the most widely deployed type of AI models?
What is the delivered token output per megawatt? For on-premises deployments especially, where capital commitment to land, power and infrastructure is substantial, maximizing intelligence produced per megawatt is critical.
Can the scale-up interconnect handle the “all-to-all” traffic of MoE models?
Is FP4 precision supported? Can the inference stack make use of FP4 while maintaining high accuracy?
Does the inference runtime support speculative decoding or multi-token prediction to increase user interactivity?
Does the serving layer support disaggregated serving, KV-aware routing, KV-cache offloading and other optimizations?
Does the platform support the unique workload requirements of agentic AI — including ultralow latency, high throughput and large input sequence lengths?
Does the platform support the full lifecycle, from training and post-training to high-scale inference, across all model architectures, to ensure infrastructure fungibility and high utilization?
Every one of these algorithmic, hardware and software optimizations must be active and integrated, or the denominator collapses. A “cheaper” GPU that delivers significantly fewer tokens per second results in a much higher cost per token. AI infrastructure that gets it right across the full stack ensures that every optimization enhances the others.
Why Does Cost per Token Matter Much More Than FLOPS per Dollar?
The following data for the DeepSeek-R1 AI model demonstrates the difference between theoretical and actual business outcomes.
Looking at compute cost alone, the NVIDIA Blackwell platform appears to cost roughly 2x more than NVIDIA Hopper — but compute cost says nothing about the output that investment buys. An analysis of mere FLOPS per dollar suggests a 2x NVIDIA Blackwell advantage compared with the NVIDIA Hopper architecture. However, the actual outcome is orders of magnitude different: Blackwell delivers more than 50x greater token output per watt than Hopper, resulting in nearly 35x lower cost per million tokens.
Note: Data is sourced from NVIDIA analysis and the SemiAnalysis InferenceX v2 benchmark.
This massive divergence proves NVIDIA Blackwell delivers a massive leap in business value over the earlier Hopper generation that far outpaces any increase in system cost.
How to Choose the Right AI Infrastructure
Comparing AI infrastructure based on compute cost or theoretical FLOPS per dollar isn't just insufficient; it doesn't provide an accurate representation of inference economics. As the data demonstrates, an accurate evaluation of AI infrastructure's revenue potential and profitability requires a shift from input metrics to cost per token and delivered token output.
NVIDIA delivers the industry's lowest token cost and highest token throughput through extreme codesign across compute, networking, memory, storage, software and partner technologies. Moreover, the constant optimization of open source inference software such as vLLM, SGLang, NVIDIA TensorRT-LLM and NVIDIA Dynamo built on the NVIDIA platform means that on existing NVIDIA infrastructure, token output continues to increase and the cost per token continues to decline long after it's acquired.
Leading cloud providers and NVIDIA cloud partners are already delivering this advantage at scale. Partners such as CoreWeave, Nebius, Nscale and Together AI have deployed NVIDIA Blackwell infrastructure and optimized their stacks to bring enterprises the lowest token cost available today, with the full benefit of NVIDIA's hardware, software and ecosystem codesign behind every interaction served. 
The Next Generation of AI Begins
It all starts here.
June 1-2 | Taipei
Register Now
Recent News
AI Infrastructure
Powering the Next American Century: US Energy Secretary Chris Wright and NVIDIA's Ian Buck on the Genesis Mission
May 7, 2026
Gaming
Linked and Loaded: Gaijin Single Sign-On Now Available on GeForce NOW
May 7, 2026
Networking
NVIDIA Spectrum-X — the Open, AI-Native Ethernet Fabric — Sets the Standard for Gigascale AI, Now With MRC
May 6, 2026
AI
NVIDIA and ServiceNow Partner on New Autonomous AI Agents for Enterprises
May 5, 2026
View All Recent News
Categories:
AI Infrastructure
Tags:
Inference
NVIDIA Blackwell
Think SMART
We were unable to load Disqus. If you are a moderator please see our troubleshooting guide.
× Comments for this thread are now closed
0 comments
1
Login
Disqus
Facebook
X (Twitter)
Google
Microsoft
Apple
6
Discussion Favorited!
Favoriting means this is a discussion worth sharing. It gets shared to your followers' Disqus feeds, and gives the creator kudos! Find More Discussions Share
Tweet this discussion
Share this discussion on Facebook
Share this discussion via email
Copy link to discussion
Best
Newest
Oldest
This discussion has been closed.
Load more comments
Subscribe Subscribed
Privacy
Do Not Sell My Data
Powered by Disqus
Related News
AI
Nemotron Labs: What OpenClaw Agents Mean for Every Organization
Apr 30, 2026
AI
NVIDIA Launches Nemotron 3 Nano Omni Model, Unifying Vision, Audio and Language for up to 9x More Efficient AI Agents
Apr 28, 2026
AI
OpenAI's New GPT-5.5 Powers Codex on NVIDIA Infrastructure — and NVIDIA Is Already Putting It to Work
Apr 23, 2026
AI
Making Sense of the Early Universe
Apr 23, 2026
Follow Us      ![](data:image/svg+xml,%3csvg id='Logo' xmlns='http://www.w3.org/2000/svg' width='108.472' height='20' viewBox='0 0 108.472 20'%3e %3cpath id='Reg' d='M1072.628,253.918v-.3h.192c.105,0,.248.008.248.136s-.073.163-.2.163h-.243m0,.211h.129l.3.524h.327l-.33-.545a.3.3,0,0,0,.311-.323c0-.285-.2-.377-.53-.377h-.482v1.245h.276v-.524m1.4-.1a1.2,1.2,0,1,0-1.2,1.157,1.14,1.14,0,0,0,1.2-1.157m-.347,0a.854.854,0,0,1-.855.891v0a.889.889,0,1,1,.855-.887Z' transform='translate(-965.557 -237.878)'/%3e %3cpath id='NVIDIA' d='M463.9,151.934v13.127h3.707V151.934Zm-29.164-.018v13.145h3.74v-10.2l2.918.01a2.674,2.674,0,0,1,2.086.724c.586.625.826,1.632.826,3.476v5.995h3.624V157.8c0-5.183-3.3-5.882-6.536-5.882Zm35.134.018v13.127h6.013c3.2,0,4.249-.533,5.38-1.727a7.352,7.352,0,0,0,1.316-4.692,7.789,7.789,0,0,0-1.2-4.516c-1.373-1.833-3.352-2.191-6.306-2.191Zm3.677,2.858h1.594c2.312,0,3.808,1.039,3.808,3.733s-1.5,3.734-3.808,3.734h-1.594Zm-14.992-2.858-3.094,10.4-2.965-10.4h-4l4.234,13.127h5.343l4.267-13.127Zm25.749,13.127h3.708V151.935h-3.709ZM494.7,151.939l-5.177,13.117h3.656l.819-2.318h6.126l.775,2.318h3.969l-5.216-13.118Zm2.407,2.393,2.246,6.145h-4.562Z' transform='translate(-399.551 -148.155)'/%3e %3cpath id='Eye_Mark' data-name='Eye Mark' d='M129.832,124.085v-1.807c.175-.013.353-.022.533-.028,4.941-.155,8.183,4.246,8.183,4.246s-3.5,4.863-7.255,4.863a4.553,4.553,0,0,1-1.461-.234v-5.478c1.924.232,2.31,1.082,3.467,3.01l2.572-2.169a6.81,6.81,0,0,0-5.042-2.462,9.328,9.328,0,0,0-1,.059m0-5.968v2.7c.177-.014.355-.025.533-.032,6.871-.232,11.348,5.635,11.348,5.635s-5.142,6.253-10.5,6.253a7.906,7.906,0,0,1-1.383-.122v1.668a9.1,9.1,0,0,0,1.151.075c4.985,0,8.59-2.546,12.081-5.559.578.463,2.948,1.591,3.435,2.085-3.319,2.778-11.055,5.018-15.44,5.018-.423,0-.829-.026-1.228-.064v2.344h18.947v-20Zm0,13.009v1.424c-4.611-.822-5.89-5.615-5.89-5.615a9.967,9.967,0,0,1,5.89-2.85v1.563h-.007a4.424,4.424,0,0,0-3.437,1.571s.845,3.035,3.444,3.908m-8.189-4.4a11.419,11.419,0,0,1,8.189-4.449v-1.463c-6.043.485-11.277,5.6-11.277,5.6s2.964,8.569,11.277,9.354v-1.555C123.731,133.451,121.643,126.728,121.643,126.728Z' transform='translate(-118.555 -118.117)' fill='%23000000'/%3e %3c/svg%3e)
United States
Privacy Policy
Your Privacy Choices
Terms of Service
Accessibility
Corporate Policies
Product Security
Contact
Copyright © 2026 NVIDIA Corporation
Share This
Facebook
LinkedIn
Share on Mastodon
Enter your Mastodon instance URL (optional) Share
NVIDIA uses cookies to improve your experience on our web site. We and our third-party partners also use cookies and other tools to collect and record information you provide as well as information about your interactions with our websites for performance improvement, analytics, and to assist in marketing efforts. By continuing to use this site or by clicking one of the buttons below, you agree to the use of cookies and other tools as described in our Privacy Policy and Cookie Policy (subject to your settings) and accept our Terms of Service (which contains important waivers). Please see our Privacy Policy for more information on our privacy practices.
We have detected the Global Privacy Control (GPC) signal and have opted you out of all optional cookies on this site for this browser. You can manage your cookie settings by clicking on "Manage Settings". Please see our Cookie Policy for more information. To opt out of non-cookie personal information "sales" / "sharing" for targeted advertising purposes, please visit the NVIDIA Preference Center. Please see our Privacy Policy for more information on our privacy practices.
We have detected the Global Privacy Control Signal (GPC) and have opted you out of all optional cookies on this browser. You can manage your cookie settings by clicking on "Manage Settings". Please see our Cookie Policy for more information. We have also opted you out of "sharing"/"sales" of personal information outside of cookies. You can manage these settings in the NVIDIA NVIDIA Preference Center. Please see our Privacy Policy for more information.
We have detected the Global Privacy Control Signal (GPC) and have opted you out of all optional cookies on this browser. You can manage your cookie settings by clicking on "Manage Settings". Please see our Cookie Policy for more information. We have also opted you out of "sharing"/"sales" of personal information outside of cookies which overrides at least one of your previous settings. You can manage them in the NVIDIA Preference Center. Please see our Privacy Policy for more information.
Manage Settings
Turn Off Optional Cookies Agree 
Cookie Settings
We and our third-party partners (including social media, advertising, and analytics partners) use cookies and other tracking technologies to collect, store, monitor, and process certain information about you when you visit our website. The information collected might relate to you, your preferences, or your device. We use that information to make the site work, analyze performance and traffic on our website, provide a more personalized web experience, and assist in our marketing efforts.
Under certain privacy laws, you have the right to direct us not to "sell" or "share" your personal information for targeted advertising. To opt-out of the "sale" and "sharing" of personal information through cookies, you must opt-out of optional cookies using the toggles below. To opt out of the "sale" and "sharing" of data collected by other means (e.g., online forms) you must also update your data sharing preferences through the NVIDIA Preference Center.
Click on the different category headings below to find out more and change the settings according to your preference. You cannot opt out of Required Cookies as they are deployed to ensure the proper functioning of our website (such as prompting the cookie banner and remembering your settings, etc.). By clicking "Save and Accept" or "Decline All" at the bottom, you consent to the use of cookies and other tools as described in our Cookie Policy in accordance with your settings and accept our Terms of Service (which contains important waivers). For more information about our privacy practices, please see our Privacy Policy.
Required Cookies
Always Active
These cookies enable core functionality such as security, network management, and accessibility. These cookies are required for the site to function and cannot be turned off.
Cookies Details
Performance Cookies [-]
Performance Cookies
These cookies are used to provide quantitative measures of our website visitors, such as the number of times you visit, time on page, your mouse movements, scrolling, clicks and keystroke activity on the websites; other browsing, search, or product research behavior; and what brought you to our site. These cookies may store a unique ID so that our system will remember you when you return. Information collected with these cookies is used to measure and find ways to improve website performance.
Cookies Details
Personalization Cookies [-]
Personalization Cookies
These cookies collect data about how you have interacted with our website to help us improve your web experience, such as which pages you have visited. These cookies may store a unique ID so that our system will remember you when you return. They may be set by us or by third party providers whose services we have added to our pages. These cookies enable us to provide enhanced website functionality and personalization as well as make the marketing messages we send to you more relevant to your interests. If you do not allow these cookies, then some or all of these services may not function properly.
Cookies Details
Advertising Cookies [-]
Advertising Cookies
These cookies record your visit to our websites, the pages you have visited and the links you have followed to influence the advertisements that you see on other websites. These cookies and the information they collect may be managed by other companies, including our advertising partners, and may be used to build a profile of your interests and show you relevant advertising on other sites. We and our advertising partners will use this information to make our websites and the advertising displayed on it, more relevant to your interests.
Cookies Details
Cookie List
Clear
[-] checkbox label label
Apply Cancel
Consent Leg.Interest [-]
checkbox label label [-]
checkbox label label [-]
checkbox label label
Decline All Save and Accept
