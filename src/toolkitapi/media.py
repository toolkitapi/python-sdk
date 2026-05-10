"""Retrieve captions/subtitles for a YouTube video."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class Media:
    """Get YouTube video transcript"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "media", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Youtube
    # ------------------------------------------------------------------ #

    def youtube_transcript(
        self,
        url: str,
        *,
        lang: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get YouTube video transcript

        Args:
            url: YouTube video URL or ID
            lang: Preferred language code
        """
        return self._client.get("youtube/transcript", params={"url": url, "lang": lang})

    def youtube_transcript_batch(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Batch transcript extraction

        Args:
            body: Request body.
        """
        return self._client.post("youtube/transcript/batch", body=body)

    def youtube_transcript_batch_status(
        self,
        job_id: str,
    ) -> Dict[str, Any]:
        """Get batch transcript job status

        Args:
            job_id: 
        """
        return self._client.get("youtube/transcript/batch/{job_id}", params={"job_id": job_id})

    def youtube_video(
        self,
        url: str,
    ) -> Dict[str, Any]:
        """Get YouTube video metadata

        Args:
            url: YouTube video URL or ID
        """
        return self._client.get("youtube/video", params={"url": url})

    def youtube_channel(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Get YouTube channel info

        Args:
            id: Channel ID, @handle, or channel URL
        """
        return self._client.get("youtube/channel", params={"id": id})

    def youtube_channel_videos(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """List channel video IDs

        Args:
            id: Channel ID, @handle, or channel URL
        """
        return self._client.get("youtube/channel/videos", params={"id": id})

    def youtube_playlist(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Get playlist info

        Args:
            id: Playlist ID or URL
        """
        return self._client.get("youtube/playlist", params={"id": id})

    def youtube_playlist_videos(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """List playlist video IDs

        Args:
            id: Playlist ID or URL
        """
        return self._client.get("youtube/playlist/videos", params={"id": id})

    def youtube_search(
        self,
        query: str,
        *,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Search YouTube

        Args:
            query: Search query
            limit: Max results
        """
        return self._client.get("youtube/search", params={"query": query, "limit": limit})

    # ------------------------------------------------------------------ #
    #  
    # ------------------------------------------------------------------ #

    def root__get(
        self,
    ) -> Dict[str, Any]:
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

    def __enter__(self) -> "Media":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
