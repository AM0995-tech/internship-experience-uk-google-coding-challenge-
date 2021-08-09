"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_playing = None
        self._paused = False
        self._playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for v in sorted(self._video_library.get_all_videos(), key=lambda v: v.title):
            print (f" {v.video()}")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video is None:
          print("Cannot play video: Video does not exist")
          return
        if self._current_playing:
          self.stop_video()
        print(f"Playing video: {video.title}")
        self._current_playing = video

    def stop_video(self):
        """Stops the current video."""
        if self._current_playing is None:
          print("Cannot stop video: No video is currently playing")
          return
        print(f"Stopping video: {self._current_playing.title}")
        self._current_playing = None
        self._paused = False


    def play_random_video(self):
        """Plays a random video from the video library."""
        v = random.choice(self._video_library.get_all_videos())
        if self._current_playing:
            self.stop_video() #no need to add a print stop section as this will to it
        print (f"Playing video: {v.title}")
        self._current_playing = v


    def pause_video(self):
        """Pauses the current video."""
        if self._paused:
            print(f"Video already paused: {self._current_playing.title}")
            return
        elif self._current_playing is None:
            print("Cannot pause video: No video is currently playing")
            return
        print(f"Pausing video: {self._current_playing.title}")
        self._paused = True


    def continue_video(self):
        """Resumes playing the current video."""
        if self._current_playing is None:
            print("Cannot continue video: No video is currently playing")
            return
        elif self._paused != True:
            print("Cannot continue video: Video is not paused")
            return
        print(f"Continuing video: {self._current_playing.title}")
        self._paused = False


    def show_playing(self):
        """Displays video currently playing."""
        if self._current_playing is None:
            print("No video is currently playing")
            return
        if self._paused:
            print(f"Currently playing: {self._current_playing.video()} - PAUSED")
        elif self._paused != True:
            print(f"Currently playing: {self._current_playing.video()}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
          print("Cannot create playlist: A playlist with the same name already exists")
          return
        print(f"Successfully created new playlist: {playlist_name}")
        self._playlists[playlist_name.lower()] = Playlist(playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video = self._video_library.get_video(video_id)
        if playlist_name.lower() not in self._playlists:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return
        if video is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        playlist = self._playlists[playlist_name.lower()]
        if video in playlist.videos:
            print(f"Cannot add video to {playlist_name}: Video already added")
            return
        playlist.videos.append(self._video_library.get_video(video_id))
        print(f"Added video to {playlist_name}: {video.title}")

    def show_all_playlists(self):
        """Display all playlists."""
        if not self._playlists :
            print("No playlists exist yet")
            return
        print("Showing all playlists:")
        for playlist in sorted(self._playlists):
          print(f"{self._playlists[playlist].name}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists:
            print (f"Cannot show playlist {playlist_name}: Playlist does not exist")
            return
        playlist = self._playlists[playlist_name.lower()]
        print(f"Showing playlist: {playlist_name}")
        if not playlist.videos:
            print("No videos here yet")
            return
        for video in playlist.videos:
            print(f"{video.video()}")




    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.lower() not in self._playlists:
            print (f"Cannot remove video from {playlist_name}: Playlist does not exist")
            return
        playlist = self._playlists[playlist_name.lower()]
        video = self._video_library.get_video(video_id)
        if not video:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return
        if video not in playlist.videos:
            print (f"Cannot remove video from {playlist_name}: Video is not in playlist")
            return
        print(f"Removed video from {playlist_name}: {video.title}")
        playlist.videos.remove(video)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return
        print(f"Successfully removed all videos from {playlist_name}")
        self._playlists[playlist_name.lower()].videos.clear()


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
            return
        print (f"Deleted playlist: {playlist_name}")
        self._playlists.clear()

    def results(self, search_result, value):
        """Display search results.

        Args:
            search_result: the result of the search
            value: the input to look for
        """
        search_result = sorted(search_result, key=lambda v: v.title)
        if not search_result:
            print(f"No search results for {value}")
            return
        print(f"Here are the results for {value}:")
        for i, vid in enumerate(search_result):
            print(f"  {i+1}) {vid.video()}")
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        selection = input()
        if not selection.isnumeric():
            return
        sel = int(selection)
        if sel < 1 or sel > len(search_result):
            return
        self.play_video(search_result[sel - 1].video_id)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        search_result = []
        for v in self._video_library.get_all_videos():
            if search_term.lower() in v.title.lower():
                search_result.append(v)
        self.results(search_result, search_term)




    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        search_result = []
        for v in self._video_library.get_all_videos():
            if video_tag.lower() in v.tags:
                search_result.append(v)
        self.results(search_result, video_tag)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
