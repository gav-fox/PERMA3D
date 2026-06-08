PERMA3D

Computational assisted permaculture CAD tool. Open source, AGPLv3.

A desktop tool that ingests real terrain and climate data for a site and uses parametric design and evolutionary algorithms to generate honest, site-specific regenerative land designs in 3D.


Motivation

I have long been interested in land regeneration and design that works with nature to improve food security and ecosystems. The idea for this project came from using Rhino3D and Grasshopper to design a greenhouse, using many parameters, Galapagos (an evolutionary fitness algorithm) and local EPW climate data. Being able to have that iterative loop where a design decision gets checked in seconds against real climate data sparked a curiosity about whether the same approach could work for earthworks and pioneer planting. The first thing a permaculture designer does is read the land, find where nature wants to hold water, and work with it. PERMA3D is my attempt to make that process computational.


What it does

Takes terrain and climate data as inputs. Computes site layers: slope, aspect, water flow, frost risk, sun hours, wind exposure. Uses those to score and evolve permaculture designs against real site conditions.

My goal is that PERMA3D meets the user with the tools they have, whether that is free national survey data or a more rigorous survey stack with LiDAR, gaussian splat capture, soil readings, species mapping, and remote sensing for a continuously updated digital twin. I believe more data should mean better design output, but that is part of what this project is trying to find out.

The visualisation is built in Godot, a game engine. The graphics might seem overkill for a land design tool but my hope is that exploring and designing within an immersive digital twin of your site will enhance the quality of design decisions. 

I am documenting this openly as I learn and make mistakes. 

For updates I am journalling this build @ JOURNAL.md. 


