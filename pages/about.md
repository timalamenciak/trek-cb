---
title: About
layout: about
permalink: /about.html
# include CollectionBuilder info at bottom
credits: true
d3: "d3"
# Edit the markdown on in this file to describe your collection
# Look in _includes/feature for options to easily add features to the page
---

<div id="myPlot">test</div>
<script>
    // Set dimensions
    const xSize = 500;
    const ySize = 500;
    const margin = 40;
    const xMax = xSize - margin * 2;
    const yMax = ySize - margin * 2;
    // Create random points
    const numPoints = 100;
    const data = [];
    for (let i = 0; i < numPoints; i++) {
        data.push([Math.random() * xMax, Math.random() * yMax]);
    }
    // Append SVG object to the page
    const svg = d3.select("div#myPlot")
        .append("svg")
        .attr("width", xSize)
        .attr("height", ySize)
        .append("g")
        .attr("transform", "translate(" + margin + "," + margin + ")");
    // X Axis
    const x = d3.scaleLinear()
        .domain([0, xMax])
        .range([0, xMax]);
    svg.append("g")
        .attr("transform", "translate(0," + yMax + ")")
        .call(d3.axisBottom(x));
    // Y Axis
    const y = d3.scaleLinear()
        .domain([0, yMax])
        .range([yMax, 0]);
    svg.append("g")
        .call(d3.axisLeft(y));
    // Dots
    svg.append('g')
        .selectAll("dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", function(d) { return d; })
        .attr("cy", function(d) { return d:inlineRefs{references="&#91;&#123;&quot;type&quot;&#58;&quot;inline_reference&quot;,&quot;start_index&quot;&#58;1682,&quot;end_index&quot;&#58;1685,&quot;number&quot;&#58;1,&quot;url&quot;&#58;&quot;https&#58;//d3-graph-gallery.com/intro_d3js.html&quot;,&quot;favicon&quot;&#58;&quot;https&#58;//imgs.search.brave.com/8WSJ1_tMM-HBVg-Bt1kd4izP_O-J11nrhkquzyGNbpw/rs&#58;fit&#58;32&#58;32&#58;1&#58;0/g&#58;ce/aHR0cDovL2Zhdmlj/b25zLnNlYXJjaC5i/cmF2ZS5jb20vaWNv/bnMvYjY3ZjU5MWUx/ZmU5MDY5MjFhZGRh/ZjQ3MTM5MTlhMDVj/ZjdiYzM4MDIyYmVl/NTk1Zjk5ZTk1YzE1/MTFiMzAwNy9kMy1n/cmFwaC1nYWxsZXJ5/LmNvbS8&quot;,&quot;snippet&quot;&#58;&quot;Usually&#32;the&#32;scale&#32;for&#32;the&#32;X&#32;axis&#32;is&#32;called&#32;x.&#32;If&#32;you&#32;run&#32;x(10),&#32;d3&#32;returns&#32;the&#32;position&#32;in&#32;px&#32;for&#32;this&#32;value&#32;→&#32;Example&#58;&#32;...&#32;Change&#32;domain&#32;and&#32;range&#32;values&#32;to&#32;understand&#32;how&#32;it&#32;works.&#32;Add&#32;a&#32;Y&#32;scale&#32;to&#32;move&#32;the&#32;circles&#32;up&#32;or&#32;down.&#32;Remember&#32;0px&#32;is&#32;on&#32;top!&#32;...&#32;These&#32;axis&#32;are&#32;always&#32;drawn&#32;on&#32;top&#32;of&#32;a&#32;scale.&#32;This&#32;scale&#32;specifies&#32;...&#32;The&#32;function&#32;axisBottom()&#32;creates&#32;a&#32;horizontal&#32;axis,&#32;with&#32;ticks&#32;and&#32;lab…&quot;&#125;&#93;"}; })
        .attr("r", 3)
        .style("fill", "Red");
</script>
{% include feature/jumbotron.html objectid="https://cdil.lib.uidaho.edu/images/palouse_sm.jpg" %} 

{% include feature/nav-menu.html sections="About CollectionBuilder CSV;About the About Page" %}


## About CollectionBuilder CSV

This demo collection features items from the University of Idaho Library's [Digital Collections](https://www.lib.uidaho.edu/digital/), and is build using [CollectionBuilder-CSV](https://github.com/CollectionBuilder/collectionbuilder-csv).

CollectionBuilder-CSV is a "Stand Alone" template for creating digital collection and exhibit websites using Jekyll, given:

- a CSV of collection metadata
- a folder of images, PDFs, audio, or video files

Driven by your collection metadata, the template generates engaging visualizations to browse and explore your objects.
The resulting static site can be hosted on any basic web server.

[CollectionBuilder](https://github.com/CollectionBuilder/) is an set of open source tools for creating digital collection and exhibit websites that are driven by metadata and powered by modern static web technology.
See [CB Docs](https://collectionbuilder.github.io/cb-docs/) for detailed information.

{% include feature/image.html objectid="demo_001" width="75" %} 

<!-- IMPORTANT!!! DELETE this comment and the include below when you are finished editing this page for your collection. The include below introduces about page features. They will show up on your collection's about page until you delete it.  -->
{% include cb/about_the_about.md %} 
