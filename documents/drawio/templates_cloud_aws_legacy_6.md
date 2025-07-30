---
title: "Aws Legacy 6 Network"
description: "A network topology diagram showing infrastructure components"
category: "templates/cloud"
type: "network"
source_file: "templates/cloud/aws_legacy_6_decoded.xml"
tags: ["cloud", "template", "architecture", "drawio", "infrastructure"]
---

# Aws Legacy 6 Network

A network topology diagram showing infrastructure components

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1422" dy="546" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="1913" value="" style="dashed=0;html=1;shape=mxgraph.aws.groups.rrect;fillColor=none;strokeColor=#000000;gradientColor=none;shadow=0;glass=0;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;strokeWidth=2;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" parent="1" vertex="1">
      <mxGeometry x="44.5" y="43.5" width="1080" height="650" as="geometry"/>
    </mxCell>
    <mxCell id="1914" value="" style="dashed=0;html=1;shape=mxgraph.aws.groups.rrect;fillColor=none;strokeColor=#000000;gradientColor=none;shadow=0;glass=0;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;strokeWidth=2;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" parent="1" vertex="1">
      <mxGeometry x="169.5" y="213.5" width="925" height="120" as="geometry"/>
    </mxCell>
    <mxCell id="1915" value="" style="rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1916" target="1936" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="354.5" y="163.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="1916" value="VPC Internet Gateway" style="dashed=0;html=1;shape=mxgraph.aws2.compute_and_networking.vpc_internet_gateway;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;whiteSpace=wrap;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="114.5" y="113.5" width="55" height="57" as="geometry"/>
    </mxCell>
    <mxCell id="1917" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1918" target="1931" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1918" value="&lt;span&gt;VPC Internet Gateway&lt;/span&gt;" style="dashed=0;html=1;shape=mxgraph.aws2.compute_and_networking.vpc_internet_gateway;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;whiteSpace=wrap;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="564.5" y="113.5" width="55" height="57" as="geometry"/>
    </mxCell>
    <mxCell id="1919" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1920" target="1934" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1920" value="&lt;span&gt;VPC Internet Gateway&lt;/span&gt;" style="dashed=0;html=1;shape=mxgraph.aws2.compute_and_networking.vpc_internet_gateway;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;whiteSpace=wrap;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="1014.5" y="113.5" width="55" height="57" as="geometry"/>
    </mxCell>
    <mxCell id="1921" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1922" target="1948" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1922" value="Device&lt;div&gt;Farm&lt;/div&gt;" style="dashed=0;html=1;shape=mxgraph.aws2.mobile_services.device_farm;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=right;labelPosition=left;verticalLabelPosition=middle;verticalAlign=middle;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="558" y="353.5" width="68" height="82" as="geometry"/>
    </mxCell>
    <mxCell id="1923" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1924" target="1943" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1924" value="SNS" style="dashed=0;html=1;shape=mxgraph.aws2.mobile_services.sns;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="1007.5" y="360" width="69" height="69" as="geometry"/>
    </mxCell>
    <mxCell id="1925" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1926" target="1949" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1926" value="" style="dashed=0;html=1;shape=mxgraph.aws2.compute_and_networking.vpc_vpn_connection;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="221.5" y="613.5" width="52" height="41" as="geometry"/>
    </mxCell>
    <mxCell id="1927" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1928" target="1949" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1928" value="" style="dashed=0;html=1;shape=mxgraph.aws2.compute_and_networking.vpc_vpn_connection;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="1016" y="613.5" width="52" height="41" as="geometry"/>
    </mxCell>
    <mxCell id="1929" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1931" target="1946" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1930" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1931" target="1922" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1931" value="HTTP Protocol" style="dashed=0;html=1;shape=mxgraph.aws2.internet_of_things.http_protocol;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;whiteSpace=wrap;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="553.5" y="248.5" width="77" height="63" as="geometry"/>
    </mxCell>
    <mxCell id="1932" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1934" target="1945" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1933" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1934" target="1924" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1934" value="Cart" style="dashed=0;html=1;shape=mxgraph.aws2.internet_of_things.cart;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=right;labelPosition=left;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="1006.5" y="244.5" width="71" height="71" as="geometry"/>
    </mxCell>
    <mxCell id="1935" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1936" target="1939" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1936" value="Code&lt;div&gt;Commit&lt;/div&gt;" style="dashed=0;html=1;shape=mxgraph.aws2.developer_tools.code_commit;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=right;labelPosition=left;verticalLabelPosition=middle;verticalAlign=middle;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="108.00000000000003" y="353.5" width="68" height="82" as="geometry"/>
    </mxCell>
    <mxCell id="1937" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1939" target="1941" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1938" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1939" target="1944" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1939" value="Machine Learning" style="dashed=0;html=1;shape=mxgraph.aws2.analytics.machine_learning;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=left;labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;whiteSpace=wrap;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="217.5" y="358.5" width="60" height="72" as="geometry"/>
    </mxCell>
    <mxCell id="1940" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1941" target="1926" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1941" value="Elastic Load Balancing" style="dashed=0;html=1;shape=mxgraph.aws2.compute_and_networking.elastic_load_balancing_2;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=right;labelPosition=left;verticalLabelPosition=middle;verticalAlign=middle;whiteSpace=wrap;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="219.5" y="483.5" width="56" height="58" as="geometry"/>
    </mxCell>
    <mxCell id="1942" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1943" target="1928" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1943" value="Elastic Load Balancing" style="dashed=0;html=1;shape=mxgraph.aws2.compute_and_networking.elastic_load_balancing_2;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=right;labelPosition=left;verticalLabelPosition=middle;verticalAlign=middle;whiteSpace=wrap;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="1014" y="483.5" width="56" height="58" as="geometry"/>
    </mxCell>
    <mxCell id="1944" value="Database" style="dashed=0;html=1;shape=mxgraph.aws2.database.dynamodb;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="218" y="244" width="59" height="72" as="geometry"/>
    </mxCell>
    <mxCell id="1945" value="Database" style="dashed=0;html=1;shape=mxgraph.aws2.database.dynamodb;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="857.5" y="244" width="59" height="72" as="geometry"/>
    </mxCell>
    <mxCell id="1946" value="RedShift DB" style="dashed=0;html=1;shape=mxgraph.aws2.database.redshift;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="428.5" y="247" width="60" height="66" as="geometry"/>
    </mxCell>
    <mxCell id="1947" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#000000;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;" parent="1" source="1948" target="1924" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="1948" value="EFS" style="dashed=0;html=1;shape=mxgraph.aws2.storage_and_content_delivery.efs;strokeColor=none;shadow=0;glass=0;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="694.5" y="358.5" width="60" height="72" as="geometry"/>
    </mxCell>
    <mxCell id="1949" value="Corporate&lt;div&gt;Network&lt;/div&gt;" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;shadow=0;glass=0;strokeColor=#23445D;strokeWidth=1;fillColor=#FFFFFF;gradientColor=none;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=middle;verticalAlign=middle;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="568.5" y="733.5" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="1950" value="" style="dashed=0;html=1;shape=mxgraph.aws.groups.aws_cloud_icon;strokeColor=none;fillColor=#F69721;gradientColor=none;shadow=0;glass=0;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="99.5" y="13.5" width="70" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="1951" value="" style="dashed=0;html=1;shape=mxgraph.aws.groups.virtual_private_cloud_icon;strokeColor=none;fillColor=#282560;gradientColor=none;shadow=0;glass=0;fontFamily=Helvetica;fontSize=12;fontColor=#23445D;align=center;labelPosition=center;verticalLabelPosition=top;verticalAlign=bottom;spacing=6;" parent="1" vertex="1">
      <mxGeometry x="179.5" y="183.5" width="70" height="40" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
