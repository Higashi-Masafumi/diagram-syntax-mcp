---
title: "Uml 1 Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/uml"
type: "flowchart"
source_file: "templates/uml/uml_1_decoded.xml"
tags: ["software", "template", "modeling", "drawio", "uml"]
---

# Uml 1 Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1.5" pageWidth="826" pageHeight="1169" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="45" value="&lt;p style=&quot;margin: 0px; margin-top: 4px; text-align: center;&quot;&gt;&lt;strong&gt;IWLayerInfoEvent&lt;/strong&gt;&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;+requestedid : int&lt;br /&gt;+requestedEvent : String&lt;br /&gt;+json : Object&lt;br /&gt;+mouseCoordinate : IWCoordinate&lt;br /&gt;+records : int&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;+toString() : String&lt;/p&gt;" style="shadow=1;fillColor=#FFCC99;gradientColor=#FFFED8;verticalAlign=top;align=left;overflow=fill;fontSize=12;fontFamily=Helvetica;html=1" parent="1" vertex="1">
      <mxGeometry x="40" y="40" width="280" height="150" as="geometry"/>
    </mxCell>
    <mxCell id="46" value="&lt;p style=&quot;margin: 0px; margin-top: 4px; text-align: center;&quot;&gt;&lt;strong&gt;IWRequestLayerEvent&lt;/strong&gt;&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;+eventName : String&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;+toString() : String&lt;/p&gt;" style="shadow=1;fillColor=#FFCC99;gradientColor=#FFFED8;verticalAlign=top;align=left;overflow=fill;fontSize=12;fontFamily=Helvetica;html=1" parent="1" vertex="1">
      <mxGeometry x="400" y="105" width="160" height="85" as="geometry"/>
    </mxCell>
    <mxCell id="47" value="&lt;p style=&quot;margin: 0px; margin-top: 4px; text-align: center;&quot;&gt;&lt;strong&gt;IWRequestLayer&lt;/strong&gt;&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;-layer : IWLayer&lt;br /&gt;-maxHits : Integer = 5&lt;br /&gt;-events : Object&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;+setMaximumHits( maxHits : Integer ) : void&lt;br /&gt;+getMaximumHits() : Integer&lt;br /&gt;+registerEvent( eventname : String ) : Boolean&lt;br /&gt;+getEvents() : Object&lt;br /&gt;+getLayer() : IWLayer&lt;br /&gt;+triggerOnRegisterEvent( event : IWRequestLayerEvent ) : void&lt;br /&gt;+triggerOnUnregisterEvent( event : IWRequestLayerEvent ) : void&lt;br /&gt;+triggerDataReceived( event : IWLayerInfoEvent ) : void&lt;/p&gt;" style="shadow=1;fillColor=#FFCC99;gradientColor=#FFFED8;verticalAlign=top;align=left;overflow=fill;fontSize=12;fontFamily=Helvetica;html=1" parent="1" vertex="1">
      <mxGeometry x="150" y="270" width="380" height="230" as="geometry"/>
    </mxCell>
    <mxCell id="57" value="&lt;&lt;use&gt;&gt;" style="endArrow=open;endSize=12;startArrow=none;startSize=10;startFill=0;edgeStyle=elbowEdgeStyle;sourcePerimeterSpacing=5;dashed=1;elbow=horizontal" parent="1" source="47" target="45" edge="1">
      <mxGeometry width="100" as="geometry">
        <mxPoint as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="60" value="&lt;&lt;use&gt;&gt;" style="endArrow=open;endSize=12;startArrow=none;startSize=10;startFill=0;edgeStyle=elbowEdgeStyle;sourcePerimeterSpacing=5;dashed=1;elbow=horizontal" parent="1" source="47" target="46" edge="1">
      <mxGeometry x="10" y="10" width="100" as="geometry">
        <mxPoint x="245" y="275" as="sourcePoint"/>
        <mxPoint x="245" y="180" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="61" value="&lt;p style=&quot;margin: 0px; margin-top: 4px; text-align: center;&quot;&gt;&lt;strong&gt;IWLayerInfoManager&lt;/strong&gt;&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;-captureSize&lt;br /&gt;-eventListeners&lt;br /&gt;-maxHits : Integer = 100&lt;br /&gt;-requestedIdCounter : int&lt;br /&gt;-requestLayers&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;-addEvent( eventName : String ) : void&lt;br /&gt;-callbackSendServerRequest( xmlHttp, eventName : String, mouseCoordinate ) : void&lt;br /&gt;-removeEvent( eventName : String ) : void&lt;br /&gt;-sendServerRequest( event : IWMouseEvent, eventName : String ) : void&lt;br /&gt;+addRequestLayer( requestLayer : IWRequestLayer ) : boolean&lt;br /&gt;+getCaptureSize()&lt;br /&gt;+getMaximumHits() : integer&lt;br /&gt;+removeRequestLayer( requestLayer : IWRequestLayer) : boolean&lt;br /&gt;+setCaptureSize( captureSize ) : void&lt;br /&gt;+setMaximumHits( maxHits : integer ) : void&lt;br /&gt;+toString() : String&lt;br /&gt;+triggerDataReceived( event : IWLayerInfoEvent ) : void&lt;/p&gt;" style="shadow=1;fillColor=#FFCC99;gradientColor=#FFFED8;verticalAlign=top;align=left;overflow=fill;fontSize=12;fontFamily=Helvetica;html=1" parent="1" vertex="1">
      <mxGeometry x="50" y="600" width="560" height="320" as="geometry"/>
    </mxCell>
    <mxCell id="63" value="request" style="endArrow=open;endSize=12;startArrow=diamond;startSize=10;startFill=0;edgeStyle=elbowEdgeStyle;sourcePerimeterSpacing=5;dashed=1;align=right;elbow=horizontal;verticalAlign=top" parent="1" source="61" target="47" edge="1">
      <mxGeometry width="100" as="geometry">
        <mxPoint as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="330" y="540"/>
          <mxPoint x="310" y="540"/>
        </Array>
        <mxPoint x="-10.5" y="32.5" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="64" value="1" style="resizable=0;align=left;verticalAlign=top;labelBackgroundColor=white;fontSize=10" parent="63" connectable="0" vertex="1">
      <mxGeometry x="-1" relative="1" as="geometry">
        <mxPoint x="8" y="-25" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="65" value="&lt;p style=&quot;margin: 0px; margin-top: 4px; text-align: center;&quot;&gt;&lt;strong&gt;IWLayer&lt;/strong&gt;&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;-map : IWMap&lt;br /&gt;-layerName : String&lt;br /&gt;-idfLayerName : String&lt;br /&gt;-shapes : Array&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;+add( node : IWNodeElement ) : void&lt;br /&gt;+expand( node : IWNodeElement ) : void&lt;br /&gt;+collapse( node : IWNodeElement ) : void&lt;br /&gt;+addLayer( node : IWNodeElement ) : void&lt;br /&gt;+setLayerName( layerName : String ) : void&lt;br /&gt;+getLayerName() : String&lt;br /&gt;+setLayerTitle( layerTitle : String ) : void&lt;br /&gt;+getLayerTitle() : String&lt;br /&gt;+getCurrentShapeName( newZoomLevel : int ) : String&lt;br /&gt;+setVisibility( visibility : Boolean ) : void&lt;br /&gt;+setIdfLayerName( idfLayerName : String ) : void&lt;br /&gt;+getidfLayerName() : String&lt;br /&gt;+addShape( shape : IWShape ) : Boolean&lt;br /&gt;+removeShape( shapeName : String ) : Boolean&lt;br /&gt;+getShapes() : Array&lt;br /&gt;+isVisible() : Boolean&lt;br /&gt;+toString() : String&lt;br /&gt;+triggerOnRemove() : void&lt;br /&gt;-updateVisiblity( newZoomLevel : int ) : void&lt;br /&gt;-updateParentVisiblity( parent : IWNodeElement ) : void&lt;/p&gt;" style="shadow=1;fillColor=#FFCC99;gradientColor=#FFFED8;verticalAlign=top;align=left;overflow=fill;fontSize=12;fontFamily=Helvetica;html=1" parent="1" vertex="1">
      <mxGeometry x="690" y="527.5" width="380" height="422.5" as="geometry"/>
    </mxCell>
    <mxCell id="67" value="&lt;p style=&quot;margin: 0px; margin-top: 4px; text-align: center;&quot;&gt;&lt;strong&gt;IWRequestLayer&lt;/strong&gt;&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;-parent : Object&lt;br /&gt;-children : Array&lt;br /&gt;-name : String&lt;br /&gt;-marked : Bolean = false&lt;br /&gt;-collapsed : Boolean = false&lt;br /&gt;+isNodeElement : Boolean = true&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;+setParent( parent : IWNodeElement ) : void&lt;br /&gt;+getParent() : IWNodeElement&lt;br /&gt;+hasChildren() : Boolean&lt;br /&gt;+hasChild( child : Object ) : Boolean&lt;br /&gt;+getChildren() : Array&lt;br /&gt;+add( node : IWNodeElement ) : void&lt;br /&gt;+remove( node : IWNodeElement ) : void&lt;br /&gt;+getName() : String&lt;br /&gt;+chackIfExistsAsParent( node : IWNodeElement ) : Boolean&lt;br /&gt;+mark() : void&lt;br /&gt;+unmark() : void&lt;br /&gt;+isMarked() : void&lt;br /&gt;+collapse() : void&lt;br /&gt;+expand() : void&lt;br /&gt;+isCollapsed() : Boolean&lt;br /&gt;+triggerStateChangedEvent() : void&lt;/p&gt;" style="shadow=1;fillColor=#FFCC99;gradientColor=#FFFED8;verticalAlign=top;align=left;overflow=fill;fontSize=12;fontFamily=Helvetica;html=1" parent="1" vertex="1">
      <mxGeometry x="690" y="40" width="380" height="422.5" as="geometry"/>
    </mxCell>
    <mxCell id="71" value="&lt;p style=&quot;margin: 0px; margin-top: 4px; text-align: center;&quot;&gt;&lt;strong&gt;IWShape&lt;/strong&gt;&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;-shapeName : String&lt;br /&gt;-range : IWRange&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;+setShapeName( shapeName : String ) : void&lt;br /&gt;+getShapeName() : String&lt;br /&gt;+setRange( range : IWRange ) : IWRange&lt;br /&gt;+getRange() : IWRange&lt;br /&gt;+toString() : String&lt;/p&gt;" style="shadow=1;fillColor=#FFCC99;gradientColor=#FFFED8;verticalAlign=top;align=left;overflow=fill;fontSize=12;fontFamily=Helvetica;html=1" parent="1" vertex="1">
      <mxGeometry x="1140" y="610" width="280" height="165" as="geometry"/>
    </mxCell>
    <mxCell id="72" value="&lt;p style=&quot;margin: 0px; margin-top: 4px; text-align: center;&quot;&gt;&lt;strong&gt;IWLayerInterface&lt;/strong&gt;&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;-useDefaults : Boolean&lt;/p&gt;&lt;hr /&gt;&lt;p style=&quot;margin: 0px; margin-left: 4px;&quot;&gt;-isVisible() : Boolean&lt;br /&gt;+setUseDefaults( useDefaults : Boolean ) : void&lt;br /&gt;+setVisible( visible : Boolean ) : void&lt;br /&gt;+useDefaults() : Boolean&lt;br /&gt;+triggerViewChangedEvent() : void&lt;/p&gt;" style="shadow=1;fillColor=#FFCC99;gradientColor=#FFFED8;verticalAlign=top;align=left;overflow=fill;fontSize=12;fontFamily=Helvetica;html=1" parent="1" vertex="1">
      <mxGeometry x="1100" y="322.5" width="280" height="145" as="geometry"/>
    </mxCell>
    <mxCell id="44" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;rounded=0;dashed=0;endArrow=block" parent="1" source="72" target="67" edge="1">
      <mxGeometry x="577.5" y="109.99999999999994" width="100" height="100" as="geometry">
        <mxPoint x="1120" y="194.99999999999994" as="sourcePoint"/>
        <mxPoint x="1300" y="124.99999999999994" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1270" y="80"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="73" value="" style="endArrow=open;endSize=12;startArrow=diamond;startSize=10;startFill=0;edgeStyle=orthogonalEdgeStyle;sourcePerimeterSpacing=5;" parent="1" source="47" target="65" edge="1">
      <mxGeometry width="100" as="geometry">
        <mxPoint as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="640" y="385"/>
          <mxPoint x="640" y="580"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="74" value="1" style="resizable=0;align=left;verticalAlign=top;labelBackgroundColor=white;fontSize=10" parent="73" connectable="0" vertex="1">
      <mxGeometry x="-1" relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="75" value="1" style="resizable=0;align=right;verticalAlign=top;labelBackgroundColor=white;fontSize=10" parent="73" connectable="0" vertex="1">
      <mxGeometry x="1" relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="76" value="" style="endArrow=open;endSize=12;startArrow=diamond;startSize=10;startFill=0;edgeStyle=orthogonalEdgeStyle;sourcePerimeterSpacing=5;" parent="1" source="65" target="72" edge="1">
      <mxGeometry width="100" as="geometry">
        <mxPoint as="sourcePoint"/>
        <mxPoint x="100" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1210" y="570"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="77" value="1" style="resizable=0;align=left;verticalAlign=top;labelBackgroundColor=white;fontSize=10" parent="76" connectable="0" vertex="1">
      <mxGeometry x="-1" relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="79" value="" style="endArrow=open;endSize=12;startArrow=diamond;startSize=10;startFill=0;edgeStyle=elbowEdgeStyle;sourcePerimeterSpacing=5;elbow=vertical" parent="1" source="65" target="71" edge="1">
      <mxGeometry x="10" y="10" width="100" as="geometry">
        <mxPoint x="1085" y="580" as="sourcePoint"/>
        <mxPoint x="1220" y="477.5" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1100" y="693"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="80" value="1" style="resizable=0;align=left;verticalAlign=top;labelBackgroundColor=white;fontSize=10" parent="79" connectable="0" vertex="1">
      <mxGeometry x="-1" relative="1" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
