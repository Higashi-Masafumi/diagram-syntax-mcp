---
title: "Aws Legacy 1 Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/cloud"
type: "flowchart"
source_file: "templates/cloud/aws_legacy_1_decoded.xml"
tags: ["cloud", "template", "architecture", "drawio", "infrastructure"]
---

# Aws Legacy 1 Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="2188" dy="840" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1.5" pageWidth="826" pageHeight="1169" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="11" value="" style="rounded=1;fillColor=none;strokeWidth=2;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" parent="1" vertex="1">
      <mxGeometry x="77" y="290" width="1333" height="570" as="geometry"/>
    </mxCell>
    <mxCell id="46" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;exitPerimeter=0;strokeColor=#CCCCCC;dashed=1;strokeWidth=3;endArrow=none" parent="1" source="6" target="21" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1281" y="750"/>
          <mxPoint x="1086" y="750"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="47" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;exitPerimeter=0;strokeColor=#CCCCCC;dashed=1;strokeWidth=3;endArrow=none" parent="1" source="6" target="20" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1281" y="750"/>
          <mxPoint x="801" y="750"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="48" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;exitPerimeter=0;strokeColor=#CCCCCC;dashed=1;strokeWidth=3;endArrow=none" parent="1" source="6" target="18" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1281" y="750"/>
          <mxPoint x="521" y="750"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="49" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;exitPerimeter=0;strokeColor=#CCCCCC;dashed=1;strokeWidth=3;endArrow=none" parent="1" source="6" target="17" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1281" y="750"/>
          <mxPoint x="239" y="750"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="18" value="Access Zone #2" style="rounded=1;fillColor=none;strokeWidth=3;strokeColor=#F7981F;dashed=1;fontColor=#F7981F;verticalLabelPosition=bottom;verticalAlign=top;fontStyle=1;fontSize=18;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" parent="1" vertex="1">
      <mxGeometry x="390" y="510" width="262" height="170" as="geometry"/>
    </mxCell>
    <mxCell id="2" value="Client Terminal #1" style="shape=mxgraph.aws.non_service_specific.client;fillColor=#C5C7C9;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="380" y="19" width="56" height="53" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="User #1" style="shape=mxgraph.aws.non_service_specific.user;fillColor=#C5C7C9;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="250" y="15" width="45" height="61" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="AWS Administrator" style="shape=mxgraph.aws.non_service_specific.user;fillColor=#C5C7C9;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="1159" y="93" width="80" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="" style="shape=mxgraph.aws.misc.aws_cloud;fillColor=#F7981F;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="140" y="240" width="100" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="AWS Server" style="shape=mxgraph.aws.non_service_specific.client;fillColor=#F7981F;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="1230" y="342" width="102.5" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="" style="shape=mxgraph.aws.compute.ec2_instances;fillColor=#FF9800;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="290" y="530.5" width="58" height="59" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="Load Dependent Scaling" style="shape=mxgraph.aws.compute.elastic_mapreduce_auto_scaling;fillColor=#FF9800;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="345" y="770" width="63" height="62" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="Access Control" style="shape=mxgraph.aws.networking.route_53;fillColor=#262261;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="1319.75" y="680" width="60" height="56" as="geometry"/>
    </mxCell>
    <mxCell id="12" value="User #2" style="shape=mxgraph.aws.non_service_specific.user;fillColor=#C5C7C9;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="250" y="99" width="45" height="61" as="geometry"/>
    </mxCell>
    <mxCell id="13" value="User #3" style="shape=mxgraph.aws.non_service_specific.user;fillColor=#C5C7C9;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="250" y="189" width="45" height="61" as="geometry"/>
    </mxCell>
    <mxCell id="14" value="Client Terminal #2" style="shape=mxgraph.aws.non_service_specific.client;fillColor=#C5C7C9;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="380" y="103" width="56" height="53" as="geometry"/>
    </mxCell>
    <mxCell id="15" value="Client Terminal #3" style="shape=mxgraph.aws.non_service_specific.client;fillColor=#C5C7C9;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="380" y="193" width="56" height="53" as="geometry"/>
    </mxCell>
    <mxCell id="16" value="Elastic Load Balancer" style="shape=mxgraph.aws.networking.elastic_load_balancer;fillColor=#262261;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="633" y="330" width="57" height="57" as="geometry"/>
    </mxCell>
    <mxCell id="17" value="Access Zone #1" style="rounded=1;fillColor=none;strokeWidth=3;strokeColor=#F7981F;dashed=1;fontColor=#F7981F;verticalLabelPosition=bottom;verticalAlign=top;fontStyle=1;fontSize=18;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" parent="1" vertex="1">
      <mxGeometry x="108" y="510" width="262" height="170" as="geometry"/>
    </mxCell>
    <mxCell id="20" value="Access Zone #3" style="rounded=1;fillColor=none;strokeWidth=3;strokeColor=#F7981F;dashed=1;fontColor=#F7981F;verticalLabelPosition=bottom;verticalAlign=top;fontStyle=1;fontSize=18;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" parent="1" vertex="1">
      <mxGeometry x="670" y="510" width="262" height="170" as="geometry"/>
    </mxCell>
    <mxCell id="21" value="Access Zone #4" style="rounded=1;fillColor=none;strokeWidth=3;strokeColor=#F7981F;dashed=1;fontColor=#F7981F;verticalLabelPosition=bottom;verticalAlign=top;fontStyle=1;fontSize=18;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" parent="1" vertex="1">
      <mxGeometry x="954.5" y="510" width="262" height="170" as="geometry"/>
    </mxCell>
    <mxCell id="24" value="Security" style="shape=mxgraph.aws.misc.virtual_private_cloud;fillColor=#F7981F;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="1321.25" y="593.25" width="60" height="34.5" as="geometry"/>
    </mxCell>
    <mxCell id="25" value="" style="shape=mxgraph.aws.on_demand_workforce.mechanical_turk_requester;fillColor=#C5C7C9;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="200" y="568.5" width="40" height="53" as="geometry"/>
    </mxCell>
    <mxCell id="26" value="" style="shape=mxgraph.aws.compute.ec2_instances;fillColor=#FF9800;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="570" y="530.5" width="58" height="59" as="geometry"/>
    </mxCell>
    <mxCell id="27" value="" style="shape=mxgraph.aws.compute.ec2_instances;fillColor=#FF9800;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="845.5" y="530.5" width="58" height="59" as="geometry"/>
    </mxCell>
    <mxCell id="28" value="" style="shape=mxgraph.aws.compute.ec2_instances;fillColor=#FF9800;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="1130" y="530.5" width="58" height="59" as="geometry"/>
    </mxCell>
    <mxCell id="29" value="" style="shape=mxgraph.aws.database.rds_mysql_db_instance;fillColor=#6F2D6E;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="480" y="571.5" width="61" height="57" as="geometry"/>
    </mxCell>
    <mxCell id="30" value="Global DNS" style="shape=mxgraph.aws.content_delivery.cloudfront;fillColor=#1EA4DD;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="1322.75" y="492.25" width="57" height="57" as="geometry"/>
    </mxCell>
    <mxCell id="31" value="" style="shape=mxgraph.aws.deployment_management.aws_elastic_beanstalk;fillColor=#296934;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="760" y="571.5" width="63" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="32" value="" style="shape=mxgraph.aws.networking.route_53_routetable;fillColor=#262261;strokeColor=none" parent="1" vertex="1">
      <mxGeometry x="1050" y="572" width="58" height="49" as="geometry"/>
    </mxCell>
    <mxCell id="33" value="Load Dependent Scaling" style="shape=mxgraph.aws.compute.elastic_mapreduce_auto_scaling;fillColor=#FF9800;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="633" y="770" width="63" height="62" as="geometry"/>
    </mxCell>
    <mxCell id="34" value="Load Dependent Scaling" style="shape=mxgraph.aws.compute.elastic_mapreduce_auto_scaling;fillColor=#FF9800;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top" parent="1" vertex="1">
      <mxGeometry x="914.5" y="770" width="63" height="62" as="geometry"/>
    </mxCell>
    <mxCell id="35" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=0;exitY=0.5;exitPerimeter=0;strokeColor=#999999;strokeWidth=3" parent="1" source="16" target="17" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="36" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.5;exitPerimeter=0;strokeColor=#999999;strokeWidth=3" parent="1" source="16" target="21" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="37" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=0.855;exitY=0.855;exitPerimeter=0;strokeColor=#999999;strokeWidth=3" parent="1" source="16" target="20" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="801" y="379"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="38" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=0.145;exitY=0.855;exitPerimeter=0;strokeColor=#999999;strokeWidth=3" parent="1" source="16" target="18" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="521" y="379"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="39" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.5;exitPerimeter=0;strokeColor=#999999;strokeWidth=3" parent="1" source="2" target="16" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="40" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.5;exitPerimeter=0;strokeColor=#999999;strokeWidth=3" parent="1" source="14" target="16" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="41" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.5;exitPerimeter=0;strokeColor=#999999;strokeWidth=3" parent="1" source="15" target="16" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="42" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.7;exitPerimeter=0;strokeColor=#F7981F;strokeWidth=4;endArrow=none" parent="1" source="4" target="6" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="43" value="" style="edgeStyle=orthogonalEdgeStyle;exitX=0;exitY=0.7;exitPerimeter=0;entryX=0.855;entryY=0.145;entryPerimeter=0;strokeColor=#F7981F;strokeWidth=4;endArrow=none" parent="1" source="4" target="16" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint y="100" as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="50" value="AWS Cloud" style="text;fontStyle=1;fontSize=14" parent="1" vertex="1">
      <mxGeometry x="1210" y="819" width="100" height="26" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
