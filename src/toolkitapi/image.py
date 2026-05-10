"""Resize an image by exact pixels or percentage, with optional aspect-ratio lock."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class Image:
    """Resize an image"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "image", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Image
    # ------------------------------------------------------------------ #

    def resize(
        self,
        url: str,
        *,
        width: Optional[int] = None,
        height: Optional[int] = None,
        maintain_aspect: Optional[bool] = None,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Resize an image

        Args:
            url: Image URL
            width: Target width in pixels
            height: Target height in pixels
            maintain_aspect: Maintain aspect ratio
            format: 
            quality: 
        """
        return self._client.get("image/resize", params={"url": url, "width": width, "height": height, "maintain_aspect": maintain_aspect, "format": format, "quality": quality})

    def crop(
        self,
        url: str,
        *,
        mode: Optional[str] = None,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Crop an image

        Args:
            url: Image URL
            mode: 'coordinates': explicit box; 'smart': center crop; 'square': largest centered square
            x: Left pixel (coordinates mode)
            y: Top pixel (coordinates mode)
            width: Crop width (coordinates mode)
            height: Crop height (coordinates mode)
            format: 
            quality: 
        """
        return self._client.get("image/crop", params={"url": url, "mode": mode, "x": x, "y": y, "width": width, "height": height, "format": format, "quality": quality})

    def rotate(
        self,
        url: str,
        degrees: float,
        *,
        expand: Optional[bool] = None,
        fill_color: Optional[str] = None,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Rotate an image

        Args:
            url: Image URL
            degrees: Rotation in degrees (clockwise positive)
            expand: Expand canvas to fit rotated image
            fill_color: Background fill colour for exposed areas (hex)
            format: 
            quality: 
        """
        return self._client.get("image/rotate", params={"url": url, "degrees": degrees, "expand": expand, "fill_color": fill_color, "format": format, "quality": quality})

    def flip(
        self,
        url: str,
        *,
        direction: Optional[str] = None,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Flip an image

        Args:
            url: Image URL
            direction: 
            format: 
            quality: 
        """
        return self._client.get("image/flip", params={"url": url, "direction": direction, "format": format, "quality": quality})

    def compress(
        self,
        url: str,
        *,
        quality: Optional[int] = None,
        format: Optional[str] = None,
    ) -> Any:
        """Compress an image

        Args:
            url: Image URL
            quality: Target quality (1=smallest, 100=lossless for PNG)
            format: 
        """
        return self._client.get("image/compress", params={"url": url, "quality": quality, "format": format})

    def strip_exif(
        self,
        url: str,
        *,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Strip EXIF metadata

        Args:
            url: Image URL
            format: 
            quality: 
        """
        return self._client.get("image/strip-exif", params={"url": url, "format": format, "quality": quality})

    def trim(
        self,
        url: str,
        *,
        tolerance: Optional[int] = None,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Auto-trim image borders

        Args:
            url: Image URL
            tolerance: Colour tolerance for border detection
            format: 
            quality: 
        """
        return self._client.get("image/trim", params={"url": url, "tolerance": tolerance, "format": format, "quality": quality})

    def pad(
        self,
        url: str,
        *,
        top: Optional[int] = None,
        right: Optional[int] = None,
        bottom: Optional[int] = None,
        left: Optional[int] = None,
        fill_color: Optional[str] = None,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Add padding to an image

        Args:
            url: Image URL
            top: Top padding in pixels
            right: Right padding in pixels
            bottom: Bottom padding in pixels
            left: Left padding in pixels
            fill_color: Padding fill colour (hex)
            format: 
            quality: 
        """
        return self._client.get("image/pad", params={"url": url, "top": top, "right": right, "bottom": bottom, "left": left, "fill_color": fill_color, "format": format, "quality": quality})

    def composite(
        self,
        base_url: str,
        overlay_url: str,
        *,
        mode: Optional[str] = None,
        opacity: Optional[float] = None,
        x: Optional[int] = None,
        y: Optional[int] = None,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Composite two images

        Args:
            base_url: Base image URL
            overlay_url: Overlay image URL
            mode: 
            opacity: Overlay opacity
            x: Overlay X offset
            y: Overlay Y offset
            format: 
            quality: 
        """
        return self._client.get("image/composite", params={"base_url": base_url, "overlay_url": overlay_url, "mode": mode, "opacity": opacity, "x": x, "y": y, "format": format, "quality": quality})

    def dither(
        self,
        url: str,
        *,
        colors: Optional[int] = None,
        format: Optional[str] = None,
    ) -> Any:
        """Reduce to a limited colour palette

        Args:
            url: Image URL
            colors: Number of palette colours
            format: 
        """
        return self._client.get("image/dither", params={"url": url, "colors": colors, "format": format})

    def remove_background(
        self,
        url: str,
        *,
        format: Optional[str] = None,
        quality: Optional[int] = None,
        alpha_matting: Optional[bool] = None,
    ) -> Any:
        """Remove image background

        Args:
            url: Image URL
            format: Output format (PNG recommended for transparency)
            quality: 
            alpha_matting: Use alpha matting for finer edge detail (slower)
        """
        return self._client.get("image/remove-background", params={"url": url, "format": format, "quality": quality, "alpha_matting": alpha_matting})

    def grayscale(
        self,
        url: str,
        *,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Convert to grayscale

        Args:
            url: Image URL
            format: 
            quality: 
        """
        return self._client.get("image/filter/grayscale", params={"url": url, "format": format, "quality": quality})

    def blur(
        self,
        url: str,
        *,
        radius: Optional[float] = None,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Apply Gaussian blur

        Args:
            url: Image URL
            radius: Gaussian blur radius in pixels
            format: 
            quality: 
        """
        return self._client.get("image/filter/blur", params={"url": url, "radius": radius, "format": format, "quality": quality})

    def sharpen(
        self,
        url: str,
        *,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Sharpen an image

        Args:
            url: Image URL
            format: 
            quality: 
        """
        return self._client.get("image/filter/sharpen", params={"url": url, "format": format, "quality": quality})

    def sepia(
        self,
        url: str,
        *,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Apply sepia tone

        Args:
            url: Image URL
            format: 
            quality: 
        """
        return self._client.get("image/filter/sepia", params={"url": url, "format": format, "quality": quality})

    def brightness(
        self,
        url: str,
        factor: float,
        *,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Adjust brightness

        Args:
            url: Image URL
            factor: Enhancement factor (1.0 = original)
            format: 
            quality: 
        """
        return self._client.get("image/adjust/brightness", params={"url": url, "factor": factor, "format": format, "quality": quality})

    def contrast(
        self,
        url: str,
        factor: float,
        *,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Adjust contrast

        Args:
            url: Image URL
            factor: Enhancement factor (1.0 = original)
            format: 
            quality: 
        """
        return self._client.get("image/adjust/contrast", params={"url": url, "factor": factor, "format": format, "quality": quality})

    def saturation(
        self,
        url: str,
        factor: float,
        *,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Adjust saturation

        Args:
            url: Image URL
            factor: Enhancement factor (1.0 = original, 0.0 = grayscale)
            format: 
            quality: 
        """
        return self._client.get("image/adjust/saturation", params={"url": url, "factor": factor, "format": format, "quality": quality})

    def placeholder(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Generate a placeholder image

        Args:
            body: Request body.
        """
        return self._client.post("image/placeholder", body=body)

    def placeholder_get(
        self,
        *,
        width: Optional[int] = None,
        height: Optional[int] = None,
        text: Optional[str] = None,
        bg_color: Optional[str] = None,
        text_color: Optional[str] = None,
        format: Optional[str] = None,
    ) -> Any:
        """Generate a placeholder image (raw)

        Args:
            width: 
            height: 
            text: 
            bg_color: 
            text_color: 
            format: 
        """
        return self._client.get("image/placeholder", params={"width": width, "height": height, "text": text, "bg_color": bg_color, "text_color": text_color, "format": format})

    def watermark_text(
        self,
        url: str,
        text: str,
        *,
        position: Optional[str] = None,
        font_size: Optional[int] = None,
        color: Optional[str] = None,
        opacity: Optional[float] = None,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Add a text watermark

        Args:
            url: Image URL
            text: 
            position: 
            font_size: 
            color: Text colour (hex)
            opacity: 
            format: 
            quality: 
        """
        return self._client.get("image/watermark/text", params={"url": url, "text": text, "position": position, "font_size": font_size, "color": color, "opacity": opacity, "format": format, "quality": quality})

    def watermark_image(
        self,
        base_url: str,
        watermark_url: str,
        *,
        position: Optional[str] = None,
        scale: Optional[float] = None,
        opacity: Optional[float] = None,
        format: Optional[str] = None,
        quality: Optional[int] = None,
    ) -> Any:
        """Add an image watermark

        Args:
            base_url: Base image URL
            watermark_url: Watermark image URL
            position: 
            scale: Watermark size as fraction of base image width
            opacity: 
            format: 
            quality: 
        """
        return self._client.get("image/watermark/image", params={"base_url": base_url, "watermark_url": watermark_url, "position": position, "scale": scale, "opacity": opacity, "format": format, "quality": quality})

    def metadata(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Extract image metadata (EXIF)

        Args:
            body: Request body.
        """
        return self._client.post("image/extract/metadata", body=body)

    def metadata_get(
        self,
        url: str,
    ) -> Any:
        """Extract image metadata from URL

        Args:
            url: Image URL
        """
        return self._client.get("image/extract/metadata", params={"url": url})

    def colors(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Extract dominant colour palette

        Args:
            body: Request body.
        """
        return self._client.post("image/extract/colors", body=body)

    def colors_get(
        self,
        url: str,
        *,
        count: Optional[int] = None,
    ) -> Any:
        """Extract colour palette from URL

        Args:
            url: Image URL
            count: Number of dominant colours to return
        """
        return self._client.get("image/extract/colors", params={"url": url, "count": count})

    def favicon(
        self,
        domain: str,
    ) -> Any:
        """Fetch highest-resolution favicon

        Args:
            domain: Domain name or URL to fetch favicon for
        """
        return self._client.get("image/favicon", params={"domain": domain})

    def download_image(
        self,
        object_name: str,
    ) -> Any:
        """Download a processed image

        Args:
            object_name: 
        """
        return self._client.get("image/download/{object_name}", params={"object_name": object_name})

    def from_html(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Render raw HTML/CSS as an image

        Args:
            body: Request body.
        """
        return self._client.post("image/from-html", body=body)

    def from_template(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Render a Liquid template as an image

        Args:
            body: Request body.
        """
        return self._client.post("image/from-template", body=body)

    def list_image_templates(
        self,
        *,
        category: Optional[str] = None,
    ) -> Dict[str, Any]:
        """List pre-built image templates

        Args:
            category: Filter templates by category. Available categories: open-graph, youtube-thumbnail, social-post, banner, professional-card, certificate.
        """
        return self._client.get("image/templates", params={"category": category})

    def get_image_template(
        self,
        template_id: str,
    ) -> Dict[str, Any]:
        """Get a single image template

        Args:
            template_id: 
        """
        return self._client.get("image/templates/{template_id}", params={"template_id": template_id})

    def convert_image(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Convert between image formats

        Args:
            body: Request body.
        """
        return self._client.post("image/convert", body=body)

    def convert_image_file(
        self,
        url: str,
        from_format: str,
        to_format: str,
        *,
        quality: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        scale: Optional[float] = None,
        background: Optional[str] = None,
        size: Optional[int] = None,
        colormode: Optional[str] = None,
        filter_speckle: Optional[int] = None,
        color_precision: Optional[int] = None,
        corner_threshold: Optional[int] = None,
        filename: Optional[str] = None,
    ) -> Any:
        """Convert image via URL (file download)

        Args:
            url: Public URL of the source image
            from_format: Source image format
            to_format: Target image format
            quality: Output quality
            width: Output width
            height: Output height
            scale: Scale factor
            background: Background colour hex
            size: ICO size
            colormode: Tracing mode (raster→SVG)
            filter_speckle: 
            color_precision: 
            corner_threshold: 
            filename: Download filename
        """
        return self._client.get("image/convert", params={"url": url, "from_format": from_format, "to_format": to_format, "quality": quality, "width": width, "height": height, "scale": scale, "background": background, "size": size, "colormode": colormode, "filter_speckle": filter_speckle, "color_precision": color_precision, "corner_threshold": corner_threshold, "filename": filename})

    # ------------------------------------------------------------------ #
    #  
    # ------------------------------------------------------------------ #

    def root__get(
        self,
    ) -> Any:
        """Root
        """
        return self._client.get("")

    # ------------------------------------------------------------------ #
    #  Status
    # ------------------------------------------------------------------ #

    def status(
        self,
    ) -> Any:
        """Status
        """
        return self._client.get("status")

    # ------------------------------------------------------------------ #
    #  Lifecycle
    # ------------------------------------------------------------------ #

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> "Image":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
