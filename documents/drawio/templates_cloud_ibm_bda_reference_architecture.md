---
title: "Ibm Bda Reference Architecture Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/cloud"
type: "flowchart"
source_file: "templates/cloud/ibm_bda_reference_architecture_decoded.xml"
tags: ["cloud", "template", "architecture", "drawio", "infrastructure"]
---

# Ibm Bda Reference Architecture Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="21" value="" style="swimlane;shadow=0;strokeColor=#4277BB;fillColor=#ffffff;fontColor=none;align=right;startSize=0;collapsible=0;noLabel=1;strokeWidth=3;" parent="1" vertex="1">
      <mxGeometry x="65" y="49" width="1040" height="730" as="geometry"/>
    </mxCell>
    <mxCell id="23" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#EDC11C;fontColor=#000000;startArrow=classic;startFill=1;strokeWidth=2;endSize=4;startSize=4;" parent="21" source="2" target="3" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="24" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.75;entryY=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;fontColor=#000000;strokeWidth=2;endSize=4;startSize=4;startArrow=classic;startFill=1;" parent="21" source="11" target="5" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="40" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.25;entryY=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;fontColor=#000000;strokeWidth=2;endSize=4;startSize=4;startArrow=classic;startFill=1;" parent="21" source="4" target="5" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="31" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.25;entryY=0;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#EDC11C;fontColor=#000000;startArrow=classic;strokeWidth=2;endSize=4;startSize=4;" parent="21" source="6" target="13" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="32" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.75;entryY=0;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#EDC11C;fontColor=#000000;startArrow=classic;strokeWidth=2;endSize=4;startSize=4;" parent="21" source="6" target="5" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="243" y="95"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="27" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;fontColor=#000000;strokeWidth=2;endSize=4;startSize=4;startArrow=classic;startFill=1;" parent="21" source="7" target="10" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="360" y="390"/>
          <mxPoint x="690" y="390"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="29" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#EDC11C;fontColor=#000000;startArrow=classic;strokeWidth=2;endSize=4;startSize=4;" parent="21" source="7" target="10" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="360" y="210"/>
          <mxPoint x="690" y="210"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="28" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;fontColor=#000000;strokeWidth=2;endSize=4;startSize=4;startArrow=classic;startFill=1;" parent="21" source="8" target="9" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="470" y="390"/>
          <mxPoint x="570" y="390"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="30" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#EDC11C;fontColor=#000000;startArrow=classic;strokeWidth=2;endSize=4;startSize=4;" parent="21" source="8" target="9" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="470" y="210"/>
          <mxPoint x="570" y="210"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="26" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;fontColor=#000000;entryX=0.75;entryY=1;strokeWidth=2;endSize=4;startSize=4;startArrow=classic;startFill=1;" parent="21" source="12" target="5" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="243" y="510"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="38" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.25;entryY=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;fontColor=#000000;strokeWidth=2;endSize=4;startSize=4;startArrow=classic;startFill=1;" parent="21" source="12" target="13" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="33" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#EDC11C;fontColor=#000000;startArrow=classic;strokeWidth=2;endSize=4;startSize=4;" parent="21" source="14" target="15" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="34" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=1;entryY=0.25;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#EDC11C;fontColor=#000000;startArrow=classic;strokeWidth=2;endSize=4;startSize=4;" parent="21" source="14" target="13" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="859.7058823529414" y="266.82352941176475" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="963" y="267"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="35" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=1;entryY=0.5;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;fontColor=#000000;strokeWidth=2;endSize=4;startSize=4;" parent="21" source="16" target="13" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="863.2352941176473" y="279.7647058823529" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="913" y="470"/>
          <mxPoint x="913" y="280"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="37" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;fontColor=#000000;strokeWidth=2;endSize=4;startSize=4;startArrow=classic;startFill=1;" parent="21" source="16" target="17" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="36" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=1;entryY=0.75;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;fontColor=#000000;strokeWidth=2;endSize=4;startSize=4;startArrow=classic;startFill=1;" parent="21" source="17" target="13" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="859.7058823529414" y="292.7058823529412" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="893" y="620"/>
          <mxPoint x="893" y="293"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="45" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#4277BB;fontSize=12;fontColor=#4277BB;strokeWidth=2;endSize=4;startSize=4;" parent="21" source="12" target="11" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2" value="CLOUD&lt;div&gt;USER&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/users/user.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;fontSize=12;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="60" y="70" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="62" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;startArrow=classic;startFill=1;startSize=4;endSize=4;jettySize=auto;orthogonalLoop=1;strokeColor=#EDC11C;strokeWidth=2;fontSize=12;fontColor=#4277BB;" parent="21" source="3" target="5" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="90" y="170"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="3" value="SaaS&lt;div&gt;APPLICATIONS&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/saas_applications.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="60" y="190" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="INTERNAL&lt;div&gt;CHANNEL&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/data_sources.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="60" y="330" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="EDGE&lt;div&gt;SERVICES&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/edge_services.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="200" y="140" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="API&lt;div&gt;MANAGEMENT&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/management/api_management.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="490" y="65" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="SaaS&lt;div&gt;APPLICATIONS&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/saas_applications.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="330" y="250" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="COGNITIVE&lt;div&gt;ANALYTICS&lt;/div&gt;&lt;div&gt;DISCOVERY &amp;amp;&lt;/div&gt;&lt;div&gt;EXPLORATION&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/analytics/analytics.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="440" y="250" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="DATA&lt;div&gt;REPOSITORY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/data_services.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="540" y="250" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="COGNITIVE&lt;div&gt;ACTIONABLE&lt;/div&gt;&lt;div&gt;INSIGHTS&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/analytics/analytics.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="660" y="250" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="11" value="STREAMING&lt;div&gt;COMPUTING&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/analytics/streaming_computing.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="290" y="401" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="12" value="DATA&lt;div&gt;INTEGRATION&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/device_registry.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="540" y="480" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="13" value="TRANSFORMATION &amp;amp;&lt;div&gt;CONNECTIVITY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/infrastructure/transformation_connectivity.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="790" y="250" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="14" value="ENTERPRISE&lt;div&gt;USER&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/users/user.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="933" y="100" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="15" value="ENTERPRISE&lt;div&gt;APPLICATIONS&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/applications/enterprise_applications.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="933" y="320" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="16" value="ENTERPRISE&lt;div&gt;DATA&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/enterprise_data.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="933" y="440" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="17" value="ENTERPRISE&lt;div&gt;USER DIRECTORY&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/data/enterprise_user_directory.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="21" vertex="1">
      <mxGeometry x="933" y="590" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="39" value="" style="swimlane;shadow=0;labelBackgroundColor=#007FFF;strokeColor=#4277BB;fillColor=none;gradientColor=none;fontColor=#000000;align=right;collapsible=0;startSize=0;strokeWidth=3;" parent="21" vertex="1">
      <mxGeometry x="210" y="590" width="650" height="120" as="geometry"/>
    </mxCell>
    <mxCell id="18" value="SECURITY" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/blockchain/certificate_authority.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="39" vertex="1">
      <mxGeometry x="170" y="10" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="19" value="INFORMATION&lt;div&gt;GOVERNANCE&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/management/information_governance.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="39" vertex="1">
      <mxGeometry x="330" y="10" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="20" value="SYSTEMS&lt;div&gt;MANAGEMENT&lt;/div&gt;" style="aspect=fixed;perimeter=ellipsePerimeter;html=1;align=center;shadow=0;dashed=0;image;image=img/lib/ibm/management/cluster_management.svg;strokeColor=#FF0000;fillColor=#FFFF66;gradientColor=none;fontColor=#4277BB;labelBackgroundColor=#ffffff;spacingTop=3;" parent="39" vertex="1">
      <mxGeometry x="497" y="10" width="60" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="22" value="PUBLIC NETWORK" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=14;spacingLeft=5;" parent="21" vertex="1">
      <mxGeometry y="10" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="43" value="" style="line;strokeWidth=3;direction=south;html=1;shadow=0;labelBackgroundColor=none;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;align=right;strokeColor=#4277BB;" parent="21" vertex="1">
      <mxGeometry x="225" width="10" height="130" as="geometry"/>
    </mxCell>
    <mxCell id="44" value="" style="line;strokeWidth=3;direction=south;html=1;shadow=0;labelBackgroundColor=none;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;align=right;strokeColor=#4277BB;" parent="21" vertex="1">
      <mxGeometry x="225" y="240" width="10" height="350" as="geometry"/>
    </mxCell>
    <mxCell id="46" value="" style="line;strokeWidth=3;direction=south;html=1;shadow=0;labelBackgroundColor=none;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;align=right;strokeColor=#4277BB;" parent="21" vertex="1">
      <mxGeometry x="820" y="350" width="10" height="240" as="geometry"/>
    </mxCell>
    <mxCell id="47" value="" style="line;strokeWidth=3;direction=south;html=1;shadow=0;labelBackgroundColor=none;fillColor=none;gradientColor=none;fontSize=12;fontColor=#4277BB;align=right;strokeColor=#4277BB;" parent="21" vertex="1">
      <mxGeometry x="820" width="10" height="240" as="geometry"/>
    </mxCell>
    <mxCell id="48" value="PROVIDER CLOUD" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=14;spacingLeft=5;" parent="21" vertex="1">
      <mxGeometry x="230" y="10" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="49" value="ENTERPRISE NETWORK" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=14;spacingLeft=5;" parent="21" vertex="1">
      <mxGeometry x="825" y="10" width="185" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="50" value="Application component" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#EBC01A;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="21" vertex="1">
      <mxGeometry x="20" y="580" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="51" value="Infrastructure services" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#8DC642;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="21" vertex="1">
      <mxGeometry x="20" y="600" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="52" value="Management" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#0DB39D;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="21" vertex="1">
      <mxGeometry x="20" y="620" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="53" value="Data store" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#335D81;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="21" vertex="1">
      <mxGeometry x="20" y="640" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="54" value="Analytics" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#744399;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="21" vertex="1">
      <mxGeometry x="20" y="660" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="55" value="Device capabilities" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#A72870;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="21" vertex="1">
      <mxGeometry x="20" y="680" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="56" value="Security" style="rounded=0;html=1;shadow=0;labelBackgroundColor=none;strokeColor=none;strokeWidth=2;fillColor=#E52134;gradientColor=none;fontSize=12;fontColor=#4277BB;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacingLeft=5;" parent="21" vertex="1">
      <mxGeometry x="20" y="700" width="20" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="59" value="LEGEND" style="text;html=1;align=left;verticalAlign=middle;fontColor=#4277BB;shadow=0;dashed=0;strokeColor=none;fillColor=none;labelBackgroundColor=none;fontStyle=1;fontSize=14;spacingLeft=0;" parent="21" vertex="1">
      <mxGeometry x="20" y="550" width="150" height="20" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
