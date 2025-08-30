from utils import read_video, save_video
from trackers import PlayerTracker, Balltracker
from drawers import PlayerTracksDrawer, BallTracksDrawer, TeamBallControlDrawer, PassInterceptionDrawer
from team_assigner import TeamAssigner
from ball_aquisition import BallAquisitionDetector
from pass_and_interception_detector import PassAndInterceptionDetector

def main():
    # Read video
    video_frames = read_video('input_videos/video_1.mp4')

    # Initialize Tracker
    player_tracker = PlayerTracker('models/player_detector_model.pt')
    ball_tracker = Balltracker('models/ball_detector_model.pt')


    # Run Trackers
    player_tracks = player_tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/player_track_stubs.pkl')
    ball_tracks = ball_tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/ball_track_stubs.pkl')


    # Remove wrong ball detections
    ball_tracks = ball_tracker.remove_wrong_detections(ball_tracks)
    # Interpolate ball tracks
    ball_tracks = ball_tracker.interpolate_ball_positions(ball_tracks)

    # Assign player teams
    team_assigner = TeamAssigner()
    player_assignment = team_assigner.get_player_teams_across_frames(video_frames, player_tracks, read_from_stub=True, stub_path='stubs/player_assignment_stub.pkl')

    # Ball Aquisition
    ball_aquisition_detector = BallAquisitionDetector()
    ball_aquisition = ball_aquisition_detector.detect_ball_possession(player_tracks, ball_tracks)

    # Detect passes and interceptions
    passes_and_interception_detector = PassAndInterceptionDetector()
    passes = passes_and_interception_detector.detect_passes(ball_aquisition, player_assignment)
    interceptions = passes_and_interception_detector.detect_interceptions(ball_aquisition, player_assignment)

    # Draw output
    # Initialize drawer
    player_tracks_drawers = PlayerTracksDrawer()
    ball_tracks_drawers = BallTracksDrawer()
    team_ball_control_drawer = TeamBallControlDrawer()
    pass_interception_drawer = PassInterceptionDrawer()

    # Draw players tracks
    output_video_frames = player_tracks_drawers.draw(video_frames,
                                                     player_tracks,
                                                     player_assignment,
                                                     ball_aquisition)
    output_video_frames = ball_tracks_drawers.draw(output_video_frames, ball_tracks)

    # Draw Team ball Control
    output_video_frames = team_ball_control_drawer.draw(output_video_frames, player_assignment, ball_aquisition)

    # Draw Passes and Interceptions
    output_video_frames = pass_interception_drawer.draw(output_video_frames, passes, interceptions)

    # Save video
    save_video('output_videos/output_video.avi', output_video_frames)

if __name__ == "__main__":
    main()