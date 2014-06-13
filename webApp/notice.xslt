<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" indent="yes"/> 

<xsl:template match="/">
	<xsl:element name="p">
		<xsl:attribute name="class">
			<xsl:text>titre</xsl:text>
		</xsl:attribute>
		<xsl:element name="a">
			<xsl:attribute name="href">
				<xsl:value-of select="$name"/>
			</xsl:attribute>
			<xsl:value-of select="$name"/>
		</xsl:element>
	</xsl:element>
	<xsl:element name="div">
		<xsl:attribute name="class">
			<xsl:text>description</xsl:text>
		</xsl:attribute>
		<xsl:for-each select="//P">
			<xsl:variable name="longueur" select="string-length(.)" />
			<xsl:if test="$longueur &gt; 6">
				<xsl:element name="p">
				   <xsl:value-of select="current()"/>
				</xsl:element>
			</xsl:if>
		</xsl:for-each>
	</xsl:element>
</xsl:template>
 
</xsl:stylesheet>
